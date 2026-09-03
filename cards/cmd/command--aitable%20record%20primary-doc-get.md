# dws aitable record primary-doc-get

kind: command
completeness: full
description: 查询记录的主键文档
source: internal/helpers/aitable.go:3560
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --record-id <String>: 目标 Record ID (必填)

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
