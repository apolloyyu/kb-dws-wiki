# dws aitable attachment remove

kind: command
completeness: full
usage: dws aitable attachment remove
description: 删除记录附件
example: dws aitable attachment remove --base-id BASE_ID --table-id TABLE_ID --record-id RECORD_ID --field-id FIELD_ID --yes
source: internal/helpers/aitable.go:4513
visible_flags: 5

## Flags
- --base-id <String>: Base ID (必填)
- --table-id <String>: Table ID (必填)
- --record-id <String>: 目标记录 ID (必填)
- --field-id <String>: 可选附件字段 ID；单独传入时清空该字段
- --resource-ids <String>: 可选附件 resourceId 列表，逗号分隔

## Related
- dws aitable attachment upload
