# dws aitable +attachment-remove

kind: shortcut
completeness: full
description: 从 attachment 字段清空全部或按文件名移除，写前确保剩余项具有可重写 fileToken，并读回验证
source: internal/shortcut/aitable/attachment_composite.go:67
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: Record ID
- --field-id <String>: attachment Field ID
- --remove-name <String>: 移除精确文件名的所有匹配项；与 --clear-all 二选一
- --clear-all <Bool>: 清空该字段全部附件；与 --remove-name 二选一

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
- dws aitable +base-copy
