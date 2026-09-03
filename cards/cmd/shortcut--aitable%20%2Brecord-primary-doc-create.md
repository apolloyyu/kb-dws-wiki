# dws aitable +record-primary-doc-create

kind: shortcut
completeness: full
description: 为记录创建主键文档（幂等），fieldId 须为 primaryDoc 类型
source: internal/shortcut/aitable/aitable.go:1005
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --field-id <String>: 主键字段 ID（primaryDoc 类型）
- --record-id <String>: 记录 ID

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
