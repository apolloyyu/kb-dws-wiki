# dws minutes list mine

kind: command
completeness: full
description: List only the meeting notes the current user created.
use_when: When the agent scopes results to the user's own recordings rather than shared ones.
source: internal/helpers/minutes.go:39
visible_flags: 1

## Flags
- --limit <Float64>: 每页数据条数 (默认 10)

## Related
- dws minutes list all
- dws minutes list shared
