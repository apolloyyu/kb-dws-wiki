# dws plugin create

kind: command
completeness: partial
usage: dws plugin create <name>
description: —
example: dws plugin create my-tool
source: internal/app/plugin_cmd.go:243
visible_flags: 1
partial_reason: missing_description

## Flags
- --description <String>: Plugin description

## Related
- dws plugin build
- dws plugin config
- dws plugin dev
- dws plugin install
