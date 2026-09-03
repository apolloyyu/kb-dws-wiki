# dws aitable +role-update

kind: shortcut
completeness: full
usage: dws aitable +role-update
description: 按 PATCH 语义增量更新自定义角色
source: internal/shortcut/aitable/aitable.go:2850
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --role-id <String>: Role ID
- --name <String>: 新角色名（可选）
- --role-type <String>: 角色类型（可选）
- --flow-type <String>: 流转类型（可选）
- --sub-roles <String>: 子角色 JSON 数组（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
