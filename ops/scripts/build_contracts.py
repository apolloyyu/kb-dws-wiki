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
from build_dws_kb import _scan_block, _top_fields, shortcut_identity


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


def literal_field(spec, name):
    fields = _top_fields(spec)
    if name not in fields:
        return None
    a, z = fields[name]
    value = spec[a:z].strip()
    if not value.startswith(('"', '`')):
        return None
    found = strings(value)
    return found[0] if found else None


def project_message_constraints(messages, enums, flag_names):
    """Literal declared-message conflicts, not general Go/runtime validation.

    Only complete mode/required-or-forbidden sentences with named schema flags
    are projected. Conditional prose, credentials categories and other shapes
    remain raw source messages; no missing condition is inferred.
    """
    rows = []
    for message in messages:
        match = re.fullmatch(r'--([a-z0-9-]+) ([A-Za-z0-9_-]+) (?:当前)?不接受 (.+)', message)
        kind = 'forbidden'
        if not match:
            match = re.fullmatch(r'--([a-z0-9-]+) ([A-Za-z0-9_-]+) 必须指定 (--[a-z0-9-]+)', message)
            kind = 'required'
        if not match or match[2] not in enums.get(match[1], []):
            continue
        flags = re.findall(r'--([a-z0-9-]+)', match[3])
        separators = re.sub(r'--[a-z0-9-]+', '', match[3])
        if not flags or not set(flags) <= flag_names or not re.fullmatch(r'[、或和/,\s]*', separators):
            continue
        rows.append({'when_flag': match[1], 'when_value': match[2], 'kind': kind,
                     'flags': flags, 'source_message': message,
                     'coverage': 'literal source validation-message declaration; not runtime execution'})
    return rows


def command_handlers(repo, source, commit):
    """Copy literal leaf handlers, matched to their own indexed definition.

    These are source excerpts, not inferred runtime contracts. Wrappers and
    transitive callees remain outside this projection.
    """
    cache, result = {}, []
    for line in (repo / 'graph/commands.jsonl').read_text().splitlines():
        row = json.loads(line)
        if not row.get('defs'):
            continue
        ref = row['defs'][0]
        path = source / ref['file']
        if not path.is_file():
            continue
        if path not in cache:
            text = path.read_text()
            literals = []
            for match in re.finditer(r'&cobra\.Command\{', text):
                spec = _scan_block(text, match.end() - 1)
                fields = _top_fields(spec)
                a, z = fields.get('Use', (0, 0))
                use = strings(spec[a:z])
                if use:
                    literals.append({'spec': spec, 'fields': fields, 'offset': match.end(),
                                     'line': text[:match.start()].count('\n') + 1,
                                     'end_line': text[:match.end() + len(spec)].count('\n') + 1,
                                     'leaf': use[0].split()[0]})
            cache[path] = (text, literals)
        text, literals = cache[path]
        candidates = [lit for lit in literals if lit['leaf'] == row['cmd'].split()[-1]
                      and lit['line'] - 3 <= ref['line'] <= lit['end_line']]
        if len(candidates) != 1:
            continue
        lit = candidates[0]
        handlers = []
        for field in ('PreRunE', 'RunE', 'PreRun', 'Run'):
            if field not in lit['fields']:
                continue
            a, z = lit['fields'][field]
            expr = lit['spec'][a:z].strip()
            if not expr.startswith('func'):
                continue  # Function references need separate call-graph coverage.
            brace = expr.find('{')
            if brace < 0:
                continue
            body = _scan_block(expr, brace)
            handlers.append({'hook': field, 'source': body,
                             'line': text[:lit['offset'] + a].count('\n') + 1})
        if handlers:
            result.append({'path': row['cmd'], 'file': ref['file'], 'source_commit': commit,
                           'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                           'handlers': handlers,
                           'coverage': 'literal leaf handler bodies only; wrappers and transitive callees not modeled'})
    return result


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
                   'enums': {}, 'required': [], 'constraints': [], 'examples': [], 'validation_messages': [],
                   'source_aliases': {}, 'source_defaults': {}, 'source_message_constraints': []}
        flag_descriptions = {}
        for match in re.finditer(r'\{\s*Name:\s*"([^"\n]+)"', spec):
            flag = _scan_block(spec, match.start())
            flag_descriptions[match[1]] = literal_field(flag, 'Desc') or ''
            default = literal_field(flag, 'Default')
            if default is not None:
                details['source_defaults'][match[1]] = default
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
        names = set(flag_descriptions)
        for name, desc in flag_descriptions.items():
            alias = re.match(r'^--([a-z0-9-]+)\s*的.*别名', desc)
            if alias and alias[1] in names and details['enums'].get(name) == details['enums'].get(alias[1]):
                details['source_aliases'][name] = alias[1]
        details['source_message_constraints'] = project_message_constraints(
            details['validation_messages'], details['enums'], names)
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
    payload = {'source_commit': commit, 'shortcuts': rows, 'commands': command_handlers(repo, source, commit), 'root_flags': global_flags,
               'coverage': 'literal source declarations; helper-injected flags and custom runtime validation are not fully modeled'}
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    return {'shortcut_contracts': len(rows), 'root_flags': len(global_flags), 'path': str(target)}


if __name__ == '__main__':
    print(json.dumps(build(*sys.argv[1:4]), ensure_ascii=False))
