"""Offline evidence-unit identity, preservation and provenance regression tests."""
import hashlib
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'bin'))
import evidence_sections as evidence
import notes_refs


def metadata(unit):
    return json.loads(unit.split('\n', 2)[1].removeprefix('evidence_unit: '))


class EvidenceUnitsTest(unittest.TestCase):
    def test_identity_binds_exact_body_and_real_source_version(self):
        body = '仅适用于 A。\r\n  value = 1  \r\n'
        unit = evidence.source_unit(body, ['https://example.invalid/source#L2'], version='v1')
        record = metadata(unit)
        self.assertEqual(unit.split('\n', 2)[2], body)
        self.assertEqual(record['body_sha256'], hashlib.sha256(body.encode()).hexdigest())
        self.assertEqual(unit, evidence.source_unit(body, record['source_refs'], version='v1'))
        changed = evidence.source_unit(body.replace('  value', 'value'), record['source_refs'], version='v1')
        self.assertNotEqual(unit.splitlines()[0], changed.splitlines()[0])

    def test_verbatim_duplicate_source_is_emitted_once(self):
        source = evidence.source_unit('same literal body', ['https://example.invalid/a'], version='v1')
        summary = evidence.source_unit('A derived interpretation.', ['notes/a.md'], kind='derived_summary')
        entries = ['== 行为语义 ==', '--- notes/a.md ---\n' + summary + '\n' + source,
                   '--- notes/b.md ---\n' + source + '\n' + summary]
        result = evidence.annotate_groups(entries)
        text = '\n'.join(result)
        self.assertEqual(text.count('same literal body'), 1)
        self.assertEqual(text.count('A derived interpretation.'), 2)
        self.assertLess(text.index('same literal body'), text.index('A derived interpretation.'))
        self.assertIn('--- notes/a.md ---', text)
        self.assertIn('--- notes/b.md ---', text)
        self.assertEqual(result, evidence.annotate_groups(result))

    def test_same_body_different_sources_and_versions_are_retained(self):
        units = [evidence.source_unit('identical text', [url], version=version)
                 for url, version in [('https://example.invalid/a', 'v1'),
                                      ('https://example.invalid/b', 'v1'),
                                      ('https://example.invalid/a', 'v2')]]
        result = evidence.annotate_groups(units)
        self.assertEqual(len(result), 3)
        self.assertEqual(len({unit.splitlines()[0] for unit in result}), 3)

    def test_heading_scope_and_qualifications_stay_with_the_source(self):
        raw = 'Only on client A.\n| field | value |\n|---|---|\n| scope | client A |\n'
        source = evidence.source_unit(raw, ['https://example.invalid/a'], scope=['# Client A', '## Limits'])
        summary = evidence.source_unit('Summary for A.', ['notes/a.md'], kind='derived_summary')
        entries = ['== unrelated ==\nother data', '--- notes/a.md ---\n' + source + '\n' + summary]
        result = evidence.annotate_groups(entries)
        selected = next(unit for unit in result if unit.startswith('== 来源证据单元'))
        self.assertEqual(selected, source)
        self.assertEqual(metadata(selected)['scope'], ['# Client A', '## Limits'])
        self.assertEqual(result[0], entries[0])
        self.assertIn('--- notes/a.md ---', result[-1])
        self.assertIn(summary, result[-1])

    def test_source_code_with_fake_group_headers_is_opaque(self):
        body = ('```markdown\n# Example\n== 行为语义 ==\n'
                '| name | value |\n|---|---|\n| x | y |\n```\nQualification after code.\n')
        source = evidence.source_unit(body, ['https://example.invalid/code'], version='fixed')
        result = '\n'.join(evidence.annotate_groups([source, source]))
        self.assertEqual(result, source)
        self.assertEqual(result.count('```'), 2)
        self.assertIn(body, result)

    def test_source_envelope_inside_source_is_not_extracted(self):
        nested = evidence.source_unit('example', ['https://example.invalid/example'])
        outer = evidence.source_unit('Documentation example:\n' + nested, ['https://example.invalid/doc'])
        self.assertEqual(evidence.annotate_groups([outer]), [outer])

    def test_fenced_source_envelope_examples_are_not_extracted(self):
        example = evidence.source_unit('EXAMPLE ONLY', ['https://example.invalid/demo'], version='example')
        for marker in ('```', '~~~', '````'):
            group = '== 篇目[1/1] docs/manual.md [docs] ==\n' + marker + 'text\n' + example + '\n' + marker
            self.assertEqual(evidence.annotate_groups([group]), [group])
            self.assertEqual(list(evidence._source_spans(group)), [])
            summary = evidence.source_unit('Actual summary.', ['notes/a.md'], kind='derived_summary')
            self.assertEqual(evidence.navigation_text(group + '\n' + summary), 'Actual summary.')

    def test_unmarked_summaries_are_not_promoted_or_deduplicated(self):
        entries = ['== Summary ==\nAccording to source X, maybe A.',
                   '== Summary ==\nAccording to source X, maybe A.']
        self.assertEqual(evidence.annotate_groups(entries), entries)
        self.assertNotIn('evidence_unit:', '\n'.join(evidence.annotate_groups(entries)))

    def test_navigation_uses_derived_text_without_promoting_it_to_source(self):
        source = evidence.source_unit('Source table: dws example list', ['https://example.invalid/a'])
        summary_body = 'Derived navigation: dws example connect'
        summary = evidence.source_unit(summary_body, ['notes/a.md'], kind='derived_summary')
        text = source + '\n' + summary
        self.assertEqual(evidence.navigation_text(text), summary_body)
        self.assertEqual(metadata(summary)['kind'], 'derived_summary')
        self.assertEqual(evidence.navigation_text(source), source)
        self.assertEqual(evidence.navigation_text('legacy input'), 'legacy input')
        tampered = summary[:-1] + '!'
        self.assertEqual(evidence.navigation_text(tampered), tampered)

    def test_tampered_metadata_does_not_authorize_deduplication(self):
        source = evidence.source_unit('A', ['https://example.invalid/a'])
        changed = source[:-1] + 'B'
        result = '\n'.join(evidence.annotate_groups([source, changed]))
        self.assertIn(source, result)
        self.assertIn(changed, result)

    def test_budget_keeps_or_defers_whole_source_with_reference(self):
        body = '```go\n' + '\tcomplete line\n' * 100 + '```\nOnly on client A.'
        source = evidence.source_unit(body, ['https://example.invalid/fixed#L1'], version='v1')
        summary = evidence.source_unit('Derived summary.', ['notes/a.md'], kind='derived_summary')
        out = evidence.pack_groups(evidence.annotate_groups([summary, source]), 800)
        self.assertLessEqual(len(out), 800)
        self.assertNotIn('\tcomplete line', out)
        self.assertIn('https://example.invalid/fixed#L1', out)
        self.assertIn('未展开完整单元', out)

    def test_budget_preserves_selected_contract_card_and_primary_document(self):
        contract = '== 命令契约: dws example connect ==\n' + 'contract flag\n' * 20
        card = '== 答案卡(card:full) ==\n' + 'selected card\n' * 20
        primary = '== 篇目[1/1] docs/example.md [docs] ==\n' + 'primary example\n' * 25
        source = evidence.source_unit('supplemental source\n' * 18, ['https://example.invalid/a'])
        summary = evidence.source_unit('derived interpretation\n' * 35,
                                       ['notes/example.md'], kind='derived_summary')
        entries = ['--- notes/example.md ---\n' + source + '\n' + summary,
                   contract, card, primary, '== 检索审计 ==\ncomplete audit']
        out = evidence.pack_groups(evidence.annotate_groups(entries), 2400)
        self.assertLessEqual(len(out), 2400)
        for body in (contract, card, primary, source):
            self.assertIn(body, out)
        self.assertNotIn('derived interpretation', out)
        self.assertIn('complete audit', out)

    def test_supplemental_source_has_priority_over_derived_note(self):
        source = evidence.source_unit('original qualification\n' * 12, ['https://example.invalid/a'])
        summary = evidence.source_unit('derived interpretation\n' * 20,
                                       ['notes/example.md'], kind='derived_summary')
        entries = ['--- notes/example.md ---\n' + summary, source]
        out = evidence.pack_groups(evidence.annotate_groups(entries), 1100)
        self.assertIn(source, out)
        self.assertNotIn('derived interpretation', out)

    def test_budget_charges_only_actual_deferred_notices(self):
        contract = '== 命令契约: dws example connect ==\n' + 'flag\n' * 100
        second = '== 命令契约: dws example other ==\n' + 'flag\n' * 100
        mechanism = '== 行为语义 ==\nimportant mechanism'
        release = '== CHANGELOG ==\nimportant release'
        result = evidence.pack_groups([contract, second, mechanism, release], 800)
        self.assertLessEqual(len(result), 800)
        self.assertIn(contract, result)
        self.assertIn(mechanism, result)
        self.assertIn(release, result)
        self.assertNotIn(second, result)

    def test_source_volume_does_not_crowd_out_selected_evidence_categories(self):
        contract = '== 命令契约: dws example connect ==\n' + 'contract flags\n' * 12
        card = '== 答案卡(card:full) ==\n' + 'selected card\n' * 12
        primary = '== 篇目[1/1] docs/example.md [docs] ==\n' + 'primary example\n' * 15
        sources = [evidence.source_unit('original qualification ' + str(i) + '\n' + 'source line\n' * 12,
                                       ['https://example.invalid/' + str(i)]) for i in range(9)]
        summary = evidence.source_unit('selected derived navigation\n' * 12,
                                       ['notes/example.md'], kind='derived_summary')
        notes = '--- notes/example.md ---\n' + summary
        entries = [contract, *sources, '\n== 行为语义(notes) ==', notes, card, primary,
                   '== 检索审计 ==\naudit']
        out = evidence.pack_groups(evidence.annotate_groups(entries), 3500)
        self.assertLessEqual(len(out), 3500)
        for body in (contract, card, primary, summary, sources[0]):
            self.assertIn(body, out)
        self.assertNotIn(sources[-1], out)
        self.assertIn('未展开完整单元', out)

    def test_category_uses_first_source_that_actually_fits(self):
        big = evidence.source_unit('BIG-SOURCE\n' + 'x' * 2000, ['https://example.invalid/big'])
        small = evidence.source_unit('SMALL-SOURCE\n' + 'x' * 100, ['https://example.invalid/small'])
        summary = evidence.source_unit('SUMMARY\n' + 'y' * 120, ['notes/a.md'], kind='derived_summary')
        out = evidence.pack_groups([big, small, summary], 800)
        self.assertLessEqual(len(out), 800)
        self.assertIn(small, out)
        self.assertNotIn('BIG-SOURCE', out)

    def test_tiny_budget_returns_short_receipt_or_explicit_minimum_error(self):
        source = evidence.source_unit('body' * 100, ['https://example.invalid/' + 'a' * 100])
        for cap in (30, 40, 80, 101):
            self.assertLessEqual(len(evidence.pack_groups([source], cap)), cap)
        for cap in (0, 10):
            with self.assertRaisesRegex(ValueError, 'at least'):
                evidence.pack_groups([source], cap)

    def test_literal_block_preserves_full_table(self):
        table = '| field | type |\r\n|---|---|\r\n| parent | Object |\r\n| child | string |\r\n'
        source = '# Object\r\n\r\n' + table + '\r\nOnly a sample.\r\n'
        block = evidence.literal_block(source, 6)
        self.assertEqual(block['body'], table)
        self.assertEqual(block['scope'], ['# Object'])
        self.assertEqual((block['line'], block['end_line']), (3, 6))

    def test_literal_block_preserves_full_code_and_real_scope(self):
        code = '```markdown\n# fake heading\nvalue\n```\n'
        source = '# Real\n## Example\n' + code
        block = evidence.literal_block(source, 5)
        self.assertEqual(block['body'], code)
        self.assertEqual(block['scope'], ['# Real', '## Example'])

    def test_literal_block_preserves_paragraph_conditions(self):
        paragraph = 'Condition A applies.\n  target value  \nCondition B also applies.\n'
        source = '# Scope\n\n' + paragraph + '\nAnother block.\n'
        self.assertEqual(evidence.literal_block(source, 4)['body'], paragraph)

    def test_heading_target_does_not_absorb_previous_section(self):
        source = '# Old\nOld-only condition.\n# New\nNew-only condition.\n'
        block = evidence.literal_block(source, 3)
        self.assertEqual(block['body'], '# New\nNew-only condition.\n')
        self.assertEqual(block['scope'], ['# New'])
        self.assertEqual((block['line'], block['end_line']), (3, 4))

    def test_list_item_preserves_continuations_and_children_without_siblings(self):
        item = '- Only when enabled: target option.\n  Continuation condition.\n  - nested limitation\n    nested continuation\n'
        source = '# Scope\n- Other item.\n' + item + '- Last item.\n'
        for line in (3, 4, 5, 6):
            block = evidence.literal_block(source, line)
            self.assertEqual(block['body'], item)
            self.assertEqual(block['scope'], ['# Scope'])

    def test_numbered_list_item_retains_blank_separated_nested_conditions(self):
        item = '2. Selected option.\n\n   Condition paragraph.\n   - nested target\n'
        source = '# Scope\n1. First option.\n' + item + '3. Last option.\n'
        self.assertEqual(evidence.literal_block(source, 6)['body'], item)

    def test_role_and_time_provenance_are_unchanged(self):
        history = ('用户：{"refresh_expires_at":"2026-08-01T10:00:00+08:00"}\n'
                   '助理：{"refresh_expires_at":"2099-01-01T00:00:00Z"}')
        timing = evidence.time_fields('执行时间是2026-07-01 12:00:00+08:00', history)
        source = evidence.source_unit('source', ['https://example.invalid/a'])
        result = evidence.annotate_groups([timing, source])
        self.assertEqual(result[0], timing)
        data = json.loads(timing.split('\n', 1)[1])
        self.assertEqual(data['timestamp_fields'], [{'origin': 'prior_user_questions',
            'path': '$[0].refresh_expires_at', 'value': '2026-08-01T10:00:00+08:00', 'kind': 'expiry'}])
        self.assertEqual(data['execution_time']['candidates_from_current_question'], ['2026-07-01 12:00:00+08:00'])
        self.assertNotIn('2099', evidence.previous_questions(history))


class NoteExpansionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        for name in ('meta', 'graph', 'docs'):
            (self.root / name).mkdir()
        self.commit = 'a' * 40
        (self.root / 'meta/MANIFEST.json').write_text(json.dumps({'source_commit': self.commit}))

    def test_source_reference_fragment_is_preserved(self):
        url = 'https://example.invalid/source?kind=one#section-a'
        for value in ('"' + url + '"', url):
            parsed = notes_refs._frontmatter(['---', 'source_url: ' + value, '---'])
            self.assertEqual(parsed['source_url'], url)

    def test_note_keeps_full_source_table_before_derived_summary(self):
        table = '| field | type |\n|---|---|\n| parent | Object |\n| child | string |\n'
        (self.root / 'docs/source.md').write_text('---\nsource_url: "https://example.invalid/source"\n'
            'updated_at: "2026-01-01"\n---\n# Scope\n' + table)
        body = ('## Derived claim\nQualified interpretation, not raw evidence.\n'
                '{{quote: docs/source.md | parent}}\n{{quote: docs/source.md | child}}\n'
                '{{quote: docs/missing.md | missing}}')
        out = notes_refs.expand(self.root, 'test.md', body, {})
        self.assertEqual(out.count(table), 1)
        self.assertLess(out.index(table), out.index('Qualified interpretation'))
        self.assertIn('"kind":"derived_summary"', out)
        self.assertIn('(原文依据: https://example.invalid/source', out)
        self.assertIn('引用原文已不存在: docs/missing.md', out)
        self.assertIn('"version":{"updated_at":"2026-01-01"}', out)

    def test_code_source_repeated_anchors_and_shared_notes_deduplicate(self):
        raw = 'func example() {\n\tfirst()\n\tsecond()\n}'
        rows = [{'path': 'a.go', 'needle': needle, 'source_commit': self.commit,
                 'line': 10, 'end_line': 13, 'source': raw,
                 'coverage': 'literal enclosing function only; callers not expanded'}
                for needle in ('first()', 'second()')]
        (self.root / 'graph/note-sources.json').write_text(json.dumps({'source_commit': self.commit, 'entries': rows}))
        body = 'Qualified interpretation.\n{{code: a.go | first()}}\n{{code: a.go | second()}}'
        shared = set()
        first = notes_refs.expand(self.root, 'a.md', body, {}, seen_sources=shared)
        second = notes_refs.expand(self.root, 'b.md', body, {}, seen_sources=shared)
        self.assertEqual((first + second).count(raw), 1)
        self.assertEqual(first.count('```'), 2)
        self.assertLess(first.index(raw), first.index('Qualified interpretation'))
        self.assertIn('callers not expanded', first)
        self.assertIn('/blob/' + self.commit + '/a.go', second)
        self.assertEqual((first + second).count('Qualified interpretation'), 2)


if __name__ == '__main__':
    unittest.main()
