# dws aitable view get

kind: command
completeness: full
description: Retrieve view definitions for a datasheet, including filter, sort, and visible-field configuration.
use_when: When the agent needs to understand or reuse a view's configuration before querying records through it.
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view list
- dws aitable view lock
- dws aitable view update
