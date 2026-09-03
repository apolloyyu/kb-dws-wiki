# dws aitable view update

kind: command
completeness: full
description: Update a view's name, filter, sort, grouping, or visible fields.
use_when: When the agent refines an existing view's configuration after inspection.
source: internal/helpers/aitable.go:1897
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 新名称，1-50 字符 (必填)
- --desc <String>: 备注文本

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view lock
