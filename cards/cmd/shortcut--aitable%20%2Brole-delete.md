# dws aitable +role-delete

kind: shortcut
completeness: full
usage: dws aitable +role-delete
description: 删除 Base 下指定的自定义角色（不可逆）
source: internal/shortcut/aitable/aitable.go:2892
visible_flags: 2

## Flags
- --base-id <String>: Base ID
- --role-id <String>: Role ID（数字 long 字符串）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
