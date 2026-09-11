# dws aitable +record-primary-doc-create

kind: shortcut
completeness: full
usage: dws aitable +record-primary-doc-create
description: 为记录创建主键文档（幂等），fieldId 须为 primaryDoc 类型
source: internal/shortcut/aitable/aitable.go:1025
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --field-id <String>: 主键字段 ID（primaryDoc 类型）
- --record-id <String>: 记录 ID
- --doc-name <String>: 可选，主键文档名称
- --template-doc-id <String>: 可选，复制该模板文档内容

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
