# dws plugin install

kind: command
completeness: partial
usage: dws plugin install
description: —
example: dws plugin install --dir ./conference
source: internal/app/plugin_cmd.go:96
visible_flags: 2
partial_reason: missing_description

## Flags
- --dir <String>: Install from a local directory
- --git <String>: Install from a Git repository

## Related
- dws plugin build
- dws plugin config
- dws plugin create
- dws plugin dev
