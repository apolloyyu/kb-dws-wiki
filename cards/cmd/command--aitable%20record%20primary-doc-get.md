# dws aitable record primary-doc-get

kind: command
completeness: full
usage: dws aitable record primary-doc-get
description: 查询记录的主键文档
example: dws aitable record primary-doc-get --base-id BASE_ID --table-id TABLE_ID --record-id RECORD_ID
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
