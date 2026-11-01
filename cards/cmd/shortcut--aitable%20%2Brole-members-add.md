# dws aitable +role-members-add

kind: shortcut
completeness: full
usage: dws aitable +role-members-add
description: 向自定义角色增量追加成员
source: internal/shortcut/aitable/aitable.go:3236
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID（String）
- --role-id <String>: 目标自定义角色 ID（long 形态 String）
- --members <String>: 增量追加，不移除现有成员；

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
