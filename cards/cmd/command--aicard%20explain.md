# dws aicard explain

kind: command
completeness: full
usage: dws aicard explain <name> [name...]
description: Inspect components, functions, Tokens, or common types
example: dws aicard explain Tabs
source: internal/helpers/aicard.go:79
visible_flags: 1

## Flags
- --compact <Bool>: Deduplicate repeated structures in batch results; single-name output is unchanged

## Related
- dws aicard lint
- dws aicard preview
