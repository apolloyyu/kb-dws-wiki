# dws aitable +role-create

kind: shortcut
completeness: full
description: 在指定 Base 下创建自定义角色
source: internal/shortcut/aitable/aitable.go:2812
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --name <String>: 角色名称
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
