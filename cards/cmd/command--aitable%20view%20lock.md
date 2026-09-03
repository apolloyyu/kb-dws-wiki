# dws aitable view lock

kind: command
completeness: full
usage: dws aitable view lock
description: 锁定/解锁视图
example: dws aitable view lock --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID
source: internal/helpers/aitable.go:4728
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标 View ID (必填)
- --off <Bool>: 解锁视图（不传则锁定）

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view update
