# dws aitable record primary-doc-create

kind: command
completeness: full
usage: dws aitable record primary-doc-create
description: 为记录创建主键文档
example: dws aitable record primary-doc-create --base-id BASE_ID --table-id TABLE_ID --field-id FIELD_ID --record-id RECORD_ID
source: internal/helpers/aitable.go:3616
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --field-id <String>: 主键字段 ID，必须是 primaryDoc 类型 (必填)
- --record-id <String>: 目标 Record ID (必填)

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
