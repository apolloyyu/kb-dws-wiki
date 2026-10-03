# dws aicard lint

kind: command
completeness: full
usage: dws aicard lint
description: Validate A2UI syntax and protocol structure
example: dws aicard lint --file card.a2ui.json --emit
source: internal/helpers/aicard.go:39
visible_flags: 5

## Flags
- --file <String>: Path to a JSON file containing an A2UI message array
- --self-check <Bool>: Check the embedded protocol, index, and local references
- --fragment <Bool>: Accept a single component, component array, or message; incompatible with --emit
- --preflight <String>: Run new-card or resources preflight after structural validation; does not send
- --emit <Bool>: On success, return a JSON string array in data.a2uiMessages; write no file

## Related
- dws aicard explain
- dws aicard preview
