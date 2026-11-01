# dws aitable +role-copy

kind: shortcut
completeness: full
usage: dws aitable +role-copy
description: 复制自定义角色配置（不复制成员）
source: internal/shortcut/aitable/aitable.go:3318
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID（String）
- --source-role-id <String>: 源自定义角色 ID（long 形态 String）；系统角色不可复制
- --name <String>: 新角色名称（String）；省略或空字符串使用「源角色名 副本」

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
