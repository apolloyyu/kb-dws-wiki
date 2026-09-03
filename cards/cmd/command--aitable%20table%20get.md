# dws aitable table get

kind: command
completeness: full
description: List datasheets within a Base, returning table IDs and names.
use_when: When the agent needs to resolve a table name to an ID inside a known Base.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable table create
- dws aitable table delete
- dws aitable table list
- dws aitable table update
