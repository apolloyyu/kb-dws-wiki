"""Compose one indexed command from JSON values, without running any command.

The caller supplies the same graph, source supplement and final declaration
checker used by dwsdoc. This module has no command-specific policy table.
"""
import csv
import io
import math
import re
import shlex


def _csv_value(items):
    """Encode one pflag StringSlice value, distinguishing [] from ['']."""
    if not items:
        return ''
    if any('\r\n' in item for item in items):
        # Go encoding/csv normalizes CRLF even inside quoted fields.
        raise ValueError('StringSlice CRLF cannot round-trip without normalization')
    stream = io.StringIO(newline='')
    csv.writer(stream, lineterminator='\r\n').writerow(items)
    encoded = stream.getvalue()[:-2]
    if next(csv.reader([encoded], strict=True)) != items:
        raise ValueError('StringSlice cannot round-trip as one CSV record')
    return encoded


def _string(value):
    if not isinstance(value, str):
        raise ValueError('requires a string; IDs and other text are not inferred')
    if '\x00' in value or any(0xD800 <= ord(c) <= 0xDFFF for c in value):
        raise ValueError('contains a character not representable in a shell argument')
    return value


def _integer(value, kind):
    if type(value) is int:
        number = value
    elif isinstance(value, str) and re.fullmatch(
            r'[+-]?(?:0[xX][0-9a-fA-F]+|0[bB][01]+|0[oO][0-7]+|0[0-7]*|[1-9][0-9]*)', value):
        sign = -1 if value.startswith('-') else 1
        digits = value.lstrip('+-')
        base = 0 if digits.lower().startswith(('0x', '0b', '0o')) else (8 if digits.startswith('0') else 10)
        number = sign * int(digits, base)
    else:
        raise ValueError('requires an integer or a supported Go integer literal')
    # Int/Uint have platform-dependent width. Check the widest Go range here;
    # the host width remains an explicit coverage gap, not an inferred fact.
    bits = int(re.search(r'\d+$', kind)[0]) if re.search(r'\d+$', kind) else 64
    unsigned = kind.startswith('u')
    low, high = (0, 2 ** bits - 1) if unsigned else (-2 ** (bits - 1), 2 ** (bits - 1) - 1)
    if not low <= number <= high:
        raise ValueError('integer outside declared type range')
    return number, [str(number)]


def _value(value, declaration):
    """Return a typed comparison value and one or more literal flag values."""
    kind = declaration.get('type', '').lower()
    if kind == 'string':
        return _string(value), [_string(value)]
    if kind == 'stringslice':
        if isinstance(value, str):
            _string(value)
            try:
                records = list(csv.reader(io.StringIO(value, newline=''), strict=True)) if value else [[]]
            except csv.Error as exc:
                raise ValueError('invalid StringSlice CSV') from exc
            if len(records) != 1:
                raise ValueError('StringSlice requires exactly one CSV record')
            items = records[0]
        elif isinstance(value, list):
            items = [_string(item) for item in value]
        else:
            raise ValueError('requires a string list or one CSV string')
        return items, [_csv_value(items)]
    if kind == 'bool':
        if type(value) is bool:
            boolean = value
        elif isinstance(value, str) and value in ('1', 't', 'T', 'TRUE', 'true', 'True', '0', 'f', 'F', 'FALSE', 'false', 'False'):
            boolean = value in ('1', 't', 'T', 'TRUE', 'true', 'True')
        else:
            raise ValueError('requires a boolean or a Go boolean literal')
        return boolean, ['true' if boolean else 'false']
    if re.fullmatch(r'u?int(?:8|16|32|64)?', kind):
        return _integer(value, kind)
    if kind in ('float32', 'float64'):
        if type(value) not in (int, float, str):
            raise ValueError('requires a finite number')
        if isinstance(value, str) and not re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?', value):
            raise ValueError('requires a supported decimal floating-point literal')
        try:
            number = float(value)
        except (ValueError, OverflowError) as exc:
            raise ValueError('requires a finite number') from exc
        if not math.isfinite(number) or (kind == 'float32' and abs(number) > 3.4028234663852886e38):
            raise ValueError('number outside supported finite type range')
        return number, [str(number)]
    # Repeated StringArray values and Duration need additional parser coverage;
    # they must not be passed through under a type-validation claim.
    raise ValueError('unsupported declared type: ' + (declaration.get('type') or 'unknown'))


def compose(payload, commands, shortcuts, details, check):
    """Return a safely quoted command only when all modeled checks pass.

    payload contains an exact canonical ``path``, the expected
    ``source_commit``, and a ``flags`` object keyed by bare declared flag names
    or shorthands. Positional arguments are currently unsupported. ``check``
    receives the complete shlex.join result, never an executed shell command.
    """
    result = {
        'argv': [], 'shell_text': None, 'source_commit': details.get('source_commit'),
        'declaration_check_pass': False, 'errors': [],
        'coverage': details.get('coverage', 'source supplement coverage unavailable'),
        'runtime_validation': 'not executed', 'checked': [],
        'unmodeled': ['custom runtime validation and service behavior',
                      'undeclared defaults, helper-injected flags, and positional arguments',
                      'StringArray, Duration, and other unsupported declared types',
                      'platform-specific width of Int/Uint within the 64-bit bound'],
    }
    errors = result['errors']
    if not isinstance(payload, dict):
        errors.append('input must be a JSON object')
        return result
    extras = set(payload) - {'path', 'source_commit', 'flags', 'args'}
    if extras:
        errors.append('unknown input fields: ' + ', '.join(sorted(map(str, extras))))
    path = payload.get('path')
    if not isinstance(path, str) or not path or path != ' '.join(path.split()):
        errors.append('path must be an exact canonical indexed command path')
        return result
    candidates = [('command', row) for row in commands if row.get('cmd') == path]
    candidates += [('shortcut', row) for row in shortcuts
                   if f"{row.get('product', '')} {row.get('cmd', '')}" == path]
    if len(candidates) != 1:
        errors.append('exact command missing or ambiguous: ' + path)
        return result
    kind, row = candidates[0]
    if kind == 'command' and any(r.get('cmd', '').startswith(path + ' ') for r in commands):
        errors.append('exact leaf required; indexed path has subcommands: ' + path)
        return result
    result['path'] = path
    supplements = [r for r in details.get('shortcuts' if kind == 'shortcut' else 'commands', [])
                   if r.get('path') == path]
    if len(supplements) > 1:
        errors.append('ambiguous source supplement: ' + path)
        return result
    supplement = supplements[0] if supplements else {}
    versions = {'contract_details': details.get('source_commit'),
                'selected_contract': supplement.get('source_commit'),
                'selected_index_row': row.get('source_commit')}
    result['source_versions'] = versions
    result['unmodeled'].append('index rows without source_commit are not independently version-verified')
    source = details.get('source_commit')
    if not isinstance(source, str) or not source:
        errors.append('source version unavailable in contract details')
    elif payload.get('source_commit') != source:
        errors.append('source version mismatch: expected ' + source)
    for scope, version in versions.items():
        if version is not None and version != source:
            errors.append('source version mismatch in ' + scope)
    supplied = payload.get('flags')
    if not isinstance(supplied, dict):
        errors.append('flags must be a JSON object')
        return result
    if 'args' in payload and (not isinstance(payload['args'], list) or payload['args']):
        errors.append('positional args unsupported; no positional values were composed')
    roots = {f['name']: f for f in details.get('root_flags', [])}
    declarations = dict(roots)
    declarations.update({f['name']: f for f in row.get('flags', [])})
    shorthands = {f['short']: f['name'] for f in declarations.values() if f.get('short')}
    aliases = supplement.get('source_aliases', {})

    def canonical(name):
        visited = set()
        while name in aliases:
            if name in visited:
                raise ValueError('cyclic source alias: ' + name)
            visited.add(name)
            name = aliases[name]
        if name not in declarations:
            raise ValueError('source alias target is not indexed: ' + name)
        return name

    values, encoded = {}, {}
    for raw_name, value in supplied.items():
        if not isinstance(raw_name, str):
            errors.append('flag names must be strings')
            continue
        name = raw_name if raw_name in declarations else shorthands.get(raw_name, raw_name)
        if name not in declarations:
            errors.append('unknown indexed flag: ' + raw_name)
            continue
        try:
            normalized, tokens = _value(value, declarations[name])
            target = canonical(name)
            if declarations[target].get('type', '').lower() != declarations[name].get('type', '').lower():
                raise ValueError('source alias type differs from canonical declaration')
            if target in values and values[target] != normalized:
                raise ValueError('conflicting alias/canonical values for --' + target)
            values[target], encoded[target] = normalized, tokens
        except ValueError as exc:
            errors.append('--' + raw_name + ': ' + str(exc))
    result['normalized_flags'] = values
    # Defaults are evidence about omitted values, not explicit flags: emitting
    # them would change Changed/presence-based constraints in the CLI.
    defaults = {name: declaration['default'] for name, declaration in declarations.items()
                if 'default' in declaration}
    defaults.update(supplement.get('source_defaults', {}))
    result['source_defaults'] = defaults
    effective = {}
    for name, value in defaults.items():
        if name not in declarations:
            errors.append('source default flag is not indexed: ' + name)
            continue
        try:
            normalized, _ = _value(value, declarations[name])
            effective[canonical(name)] = normalized
        except ValueError as exc:
            errors.append('source default --' + name + ': ' + str(exc))
    effective.update(values)
    result['effective_flags'] = effective
    required = {f['name'] for f in declarations.values() if f.get('required')}
    required.update(supplement.get('required', []))
    for name in sorted(required):
        try:
            target = canonical(name)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if target not in values or values[target] in ('', []):
            errors.append('missing or empty required: ' + name)
    if errors:
        return result
    argv = ['dws', *path.split()]
    for name in sorted(encoded):
        # The equals form also preserves values beginning with '--'. Bool false
        # is explicit and cannot accidentally become a separate positional.
        argv.extend('--' + name + '=' + token for token in encoded[name])
    shell_text = shlex.join(argv)
    if shlex.split(shell_text) != argv:
        errors.append('shell argument round-trip failed')
        return result
    checked = check(shell_text)
    result['checked'] = ['exact indexed leaf', 'declared source versions',
                         'supported flag types and required nonempty values',
                         'declared aliases and conflicting values',
                         'shell argument round-trip', 'complete command declaration check']
    if not isinstance(checked, dict):
        errors.append('declaration checker returned an invalid result')
        return result
    errors.extend(checked.get('errors', []))
    if checked.get('error'):
        errors.append(checked['error'])
    errors.extend('unknown indexed flag: ' + name for name in checked.get('unknown_indexed_flags', []))
    if checked.get('path') not in (None, path):
        errors.append('declaration checker resolved a different command path')
    if not checked.get('declaration_check_pass') and not errors:
        errors.append('complete command declaration check failed')
    if not errors:
        result.update(argv=argv, shell_text=shell_text, declaration_check_pass=True)
    return result
