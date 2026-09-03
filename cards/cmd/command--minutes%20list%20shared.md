# dws minutes list shared

kind: command
completeness: full
usage: dws minutes list shared
description: List meeting notes that have been shared with the current user by others.
example: dws minutes list shared
use_when: When the agent wants to surface meetings the user is an invited viewer of.
source: internal/helpers/minutes.go:86
visible_flags: 1

## Flags
- --limit <Float64>: 每页数据条数 (默认 10)

## Related
- dws minutes list all
- dws minutes list mine
