# dws minutes list shared

kind: command
completeness: full
description: List meeting notes that have been shared with the current user by others.
use_when: When the agent wants to surface meetings the user is an invited viewer of.
source: internal/helpers/minutes.go:86
visible_flags: 1

## Flags
- --limit <Float64>: 每页数据条数 (默认 10)

## Related
- dws minutes list all
- dws minutes list mine
