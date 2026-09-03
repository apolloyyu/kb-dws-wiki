# dws plugin dev

kind: command
completeness: partial
usage: dws plugin dev <dir>
description: —
example: dws plugin dev ./my-tool
source: internal/app/plugin_cmd.go:365
visible_flags: 1
partial_reason: missing_description

## Flags
- --off <Bool>: Unregister a dev plugin

## Related
- dws plugin build
- dws plugin config
- dws plugin create
- dws plugin install
