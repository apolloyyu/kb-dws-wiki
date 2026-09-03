# dws aitable record query-empty

kind: command
completeness: full
usage: dws aitable record query-empty
description: 查询完全没填用户字段的空行
example: dws aitable record query-empty --base-id BASE_ID --table-id TABLE_ID
source: internal/helpers/aitable.go:3299
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --limit <Int>: 单次扫描的最大记录数（扫描预算，非返回数）；范围 [1, 100]，默认 100
- --cursor <String>: 分页游标。首次不传；返回 nextCursor 非空时把它传回继续扫

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
