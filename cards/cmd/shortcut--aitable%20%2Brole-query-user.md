# dws aitable +role-query-user

kind: shortcut
completeness: full
usage: dws aitable +role-query-user
description: 查询用户实际命中的高级权限角色
source: internal/shortcut/aitable/aitable.go:3346
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID（String）
- --target-uid <String>: 目标用户 uid（long 形态 String，不是 userId）；可选，省略或空字符串查询当前调用人，不替换调用身份

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
