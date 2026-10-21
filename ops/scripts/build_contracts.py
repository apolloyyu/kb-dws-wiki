#!/usr/bin/env python3
"""Deterministic source supplements for existing command/shortcut contracts.

No command-specific rules or generated prose: all examples, enum values and
validation messages are literal source strings, attached to their own command.
"""
import hashlib
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_dws_kb import _scan_block, shortcut_identity


def strings(text):
    result = []
    for m in re.finditer(r'"(?:[^"\\]|\\.)*"|`[^`]*`', text, re.S):
        try:
            result.append(m[0][1:-1] if m[0].startswith('`') else json.loads(m[0]))
        except ValueError:
            continue
    return result


def literal_block(text, name):
    match = re.search(r'\b' + name + r':\s*\[\][\w.]+\s*\{', text)
    return _scan_block(text, match.end() - 1) if match else ''


def build(repo, source, commit):
    repo, source = pathlib.Path(repo), pathlib.Path(source)
    rows = []
    for line in (repo / 'graph/shortcuts.jsonl').read_text().splitlines():
        row = json.loads(line)
        path = source / row['file']
        if not path.is_file():
            continue
        text = path.read_text()
        anchor = re.search(r'\bCommand:\s*' + re.escape(json.dumps(row['cmd'])), text)
        if not anchor:
            continue
        start = text.rfind('shortcut.Shortcut{', 0, anchor.start())
        if start < 0:
            continue
        brace = text.index('{', start)
        spec = _scan_block(text, brace)
        identity = shortcut_identity(text, spec)
        if identity != (row['product'], row['cmd']):
            raise ValueError('Graph/source shortcut identity mismatch: ' + str(identity))
        details = {'path': f"{row['product']} {row['cmd']}", 'file': row['file'],
                   'source_commit': commit, 'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                   'enums': {}, 'required': [], 'constraints': [], 'examples': [], 'validation_messages': []}
        for match in re.finditer(r'\{\s*Name:\s*"([^"\n]+)"', spec):
            flag = _scan_block(spec, match.start())
            enum = strings(literal_block(flag, 'Enum'))
            if enum:
                details['enums'][match[1]] = enum
            if re.search(r'\bRequired:\s*true\b', flag):
                details['required'].append(match[1])
        for match in re.finditer(r'\b(?:Examples|Tips):\s*(?:\[\]string\s*)?\{', spec):
            details['examples'].extend(strings(_scan_block(spec, match.end() - 1)))
        details['examples'] = list(dict.fromkeys(details['examples']))
        for match in re.finditer(r'\{\s*Kind:\s*shortcut\.Constraint(AtLeastOne|MutuallyExclusive)', spec):
            block = _scan_block(spec, match.start())
            flags = strings(literal_block(block, 'Flags'))
            if flags:
                details['constraints'].append({'kind': match[1], 'flags': flags})
        validate = re.search(r'\bValidate:\s*(\w+)\s*,', spec)
        if validate:
            fn = re.search(r'(?m)^func\s+' + re.escape(validate[1]) + r'\(', text)
            if fn:
                body = _scan_block(text, text.index('{', fn.start()))
                for match in re.finditer(r'(?:NewValidation|Errorf|New)\(\s*("(?:[^"\\]|\\.)*")', body):
                    message = strings(match[1])
                    if message:
                        details['validation_messages'].append(message[0])
        rows.append(details)
    global_flags = []
    root_path = source / 'internal/app/flags.go'
    if root_path.is_file():
        text = root_path.read_text()
        for match in re.finditer(r'\.PersistentFlags\(\)\.(\w+)\(', text):
            line = text[match.end():].split('\n', 1)[0]
            args = strings(line)
            if not args or not match[1].endswith(('Var', 'VarP')):
                continue
            global_flags.append({'name': args[0], 'short': args[1] if match[1].endswith('P') else '',
                                 'type': match[1].split('Var')[0], 'help': args[-1],
                                 'file': 'internal/app/flags.go', 'line': text[:match.start()].count('\n') + 1})
    target = repo / 'graph/contract-details.json'
    payload = {'source_commit': commit, 'shortcuts': rows, 'root_flags': global_flags,
               'coverage': 'literal source declarations; helper-injected flags and custom runtime validation are not fully modeled'}
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    return {'shortcut_contracts': len(rows), 'root_flags': len(global_flags), 'path': str(target)}


if __name__ == '__main__':
    print(json.dumps(build(*sys.argv[1:4]), ensure_ascii=False))
