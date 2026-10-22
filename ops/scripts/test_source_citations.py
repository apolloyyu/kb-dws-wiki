"""Copyable source citations, without network or DWS business execution."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'bin'))
import notes_refs
import evidence_sections

DOC = runpy.run_path(str(ROOT / 'bin/dwsdoc'))
LINK = re.compile(r'\[((?:\\.|[^\]\\])+)\]\(([^\s()]*)\)')


class SourceCitationTest(unittest.TestCase):
    def cli(self, *args):
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'bin/dwsdoc'), *args],
                                text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return result.stdout

    def test_fixed_source_url_keeps_commit_line_and_escapes(self):
        url = 'https://github.com/owner/repo/blob/abc1234/internal/a.go#L993'
        self.assertEqual(notes_refs.source_citation(url), '[DWS 源码依据](' + url + ')')
        awkward = 'https://example.invalid/a (copy)/中文%20name?q=a(b)&x=1#L19'
        link = notes_refs.source_citation(awkward, 'dws [item] \\ *name*\n来源')
        match = LINK.fullmatch(link)
        self.assertIsNotNone(match, link)
        self.assertIn(r'\[item\]', match[1])
        self.assertIn(r'\\', match[1])
        self.assertNotIn('%2520', match[2])
        self.assertEqual(unquote(match[2]), unquote(awkward))
        self.assertTrue(match[2].endswith('#L19'))
        self.assertEqual(notes_refs.source_citation('notes/internal.md'), '无(未提供公开来源)')

    def test_all_cli_citation_surfaces_return_semantic_markdown_labels(self):
        for args in [('contract', 'auth reset'), ('cmd', 'auth reset'),
                     ('short', '+messages-send'), ('card', 'auth reset'),
                     ('ctx', 'dws auth reset'), ('ctx', 'dws 登录态多久过期'),
                     ('cat', 'docs/products/event.md')]:
            with self.subTest(args=args):
                output = self.cli(*args)
                lines = [line.strip() for line in output.splitlines()
                         if line.strip().startswith('引用: ') and 'https://' in line]
                self.assertTrue(lines, args)
                for line in lines:
                    match = LINK.fullmatch(line.removeprefix('引用: '))
                    self.assertIsNotNone(match, line)
                    self.assertNotRegex(match[1], r'\.go|\.md|#L\d|internal/|docs/|notes/')
                self.assertNotRegex(output, r'(?m)^\s*引用: https?://')

    def test_show_command_flag_location_is_a_link_not_a_path_label(self):
        row = {'cmd': 'example list', 'desc': 'example', 'defs': [], 'flags': [
            {'name': 'mode', 'type': 'String', 'help': 'mode',
             'file': 'internal/example.go', 'line': 9}]}
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            DOC['show_cmd'](row)
        text = output.getvalue()
        self.assertIn('[DWS 源码依据](https://', text)
        self.assertNotIn('[internal/example.go:9]', text)

    def test_notes_preserve_raw_body_metadata_version_and_verified_hash(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ('meta', 'graph', 'docs'):
                (root / name).mkdir()
            commit = 'a' * 40
            (root / 'meta/MANIFEST.json').write_text(json.dumps({'source_commit': commit}))
            code = 'func example() {\n\tfirst()\n\tsecond()\n}'
            raw = {'path': 'internal/example.go', 'needle': 'first()', 'source_commit': commit,
                   'line': 9, 'end_line': 12, 'source': code, 'coverage': 'literal enclosing function only'}
            (root / 'graph/note-sources.json').write_text(json.dumps({'source_commit': commit, 'entries': [raw]}))
            literal = '| field | type |\r\n|---|---|\r\n| value | string |\r\n'
            doc_url = 'https://example.invalid/a%20b?q=x#section'
            (root / 'docs/source.md').write_bytes(('---\nsource_url: "' + doc_url + '"\n'
                'updated_at: "2026-01-01"\n---\n# Scope\n').encode() + literal.encode())
            body = '{{code: internal/example.go | first()}}\n{{quote: docs/source.md | value}}'
            checks = {('test.md', 'code', 'internal/example.go | first()'): {'ok': True, 'line': 9}}
            output = notes_refs.expand(root, 'test.md', body, checks)
            source_url = notes_refs.GH.replace('/main/', '/' + commit + '/') + 'internal/example.go#L9'
            self.assertNotIn('source_url: ' + source_url + '\n', output)
            self.assertIn('```go\n' + code + '\n```', output)
            self.assertIn(literal, output)
            self.assertIn('引用: [源码依据](' + source_url + ')', output)
            self.assertIn('[源码依据](' + source_url + ')', output)
            self.assertIn('[原文依据](' + doc_url + ')', output)
            source_units = [(start, end, meta) for start, end, meta in evidence_sections._source_spans(output)
                            if meta['kind'] == 'source']
            self.assertEqual(len(source_units), 2)
            self.assertEqual({ref for _, _, meta in source_units for ref in meta['source_refs']},
                             {source_url, doc_url})
            for start, end, meta in source_units:
                exact_body = output[end - meta['body_chars']:end]
                self.assertEqual(meta['body_sha256'], hashlib.sha256(exact_body.encode()).hexdigest())
                if code in exact_body:
                    # The sole human URL replaces the old source_url line at
                    # the same size; metadata remains the raw machine mapping.
                    legacy = 'source_url: ' + source_url + '\ncoverage: ' + raw['coverage'] + '\n```go\n' + code + '\n```'
                    self.assertEqual(len(exact_body), len(legacy))
                    self.assertEqual(exact_body.count(source_url), 1)
            self.assertTrue(any(meta['version'] == commit for _, _, meta in source_units))
            self.assertTrue(any(meta['version'] == {'updated_at': '2026-01-01'} for _, _, meta in source_units))

    def test_card_keeps_internal_source_metadata_while_adding_copyable_citation(self):
        output = self.cli('card', 'auth reset')
        card = (ROOT / 'cards/cmd/command--auth%20reset.md').read_text()
        self.assertIn(card.strip(), output)
        self.assertIn('[DWS 源码依据](https://', output)

    def test_real_rate_limit_budget_keeps_all_original_functions(self):
        output = self.cli('ctx', 'dws RATE_LIMIT_ERROR 是什么，retryable 代表自动重试吗？')
        units = [(output[end - meta['body_chars']:end], meta)
                 for _, end, meta in evidence_sections._source_spans(output) if meta['kind'] == 'source']
        entries = json.loads((ROOT / 'graph/note-sources.json').read_text())['entries']
        anchors = [('internal/app/server_failure_classifier.go', 131),
                   ('internal/transport/diagnostics.go', 151),
                   ('internal/transport/diagnostics.go', 40),
                   ('internal/transport/client.go', 1008)]
        for path, line in anchors:
            raw = next(row for row in entries if row['path'] == path and row['line'] == line)
            body = next(body for body, meta in units if any(ref.endswith(path + '#L' + str(line))
                                                         for ref in meta['source_refs']))
            self.assertIn('```go\n' + raw['source'] + '\n```', body)
        self.assertLessEqual(len(output), 20001)  # print's trailing newline


if __name__ == '__main__':
    unittest.main()
