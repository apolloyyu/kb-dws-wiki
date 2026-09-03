# dws aitable view duplicate

kind: command
completeness: full
description: 复制视图
source: internal/helpers/aitable.go:5034
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 源 View ID (必填)
- --new-name <String>: 新视图名称（不传则由 server 默认命名）

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view get
- dws aitable view list
- dws aitable view lock
- dws aitable view update
