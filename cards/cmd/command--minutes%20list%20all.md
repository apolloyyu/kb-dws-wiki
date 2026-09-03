# dws minutes list all

kind: command
completeness: full
description: List all meeting notes the user has access to, filterable by keyword and time range.
use_when: When the agent needs a broad search across the user's full minutes library.
source: internal/helpers/minutes.go:132
visible_flags: 1

## Flags
- --limit <Float64>: 每页数据条数 (默认 10)

## Related
- dws minutes list mine
- dws minutes list shared
