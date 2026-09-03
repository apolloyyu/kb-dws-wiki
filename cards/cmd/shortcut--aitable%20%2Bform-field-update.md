# dws aitable +form-field-update

kind: shortcut
completeness: full
description: 更新表单字段的必填状态或描述
source: internal/shortcut/aitable/aitable.go:1849
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-id <String>: 表单 View ID
- --field-id <String>: Field ID
- --required <Bool>: 是否必填（可选）
- --field-description <String>: 字段描述（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
