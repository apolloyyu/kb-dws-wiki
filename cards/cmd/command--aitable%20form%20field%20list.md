# dws aitable form field list

kind: command
completeness: full
usage: dws aitable form field list
description: 列出表单字段
example: dws aitable form field list --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID
source: internal/helpers/aitable.go:5463
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)

## Related
- dws aitable form field hide
- dws aitable form field update
