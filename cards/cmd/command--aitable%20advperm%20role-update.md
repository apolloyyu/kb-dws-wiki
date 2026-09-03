# dws aitable advperm role-update

kind: command
completeness: full
description: 增量更新自定义角色配置（patch 语义）
source: internal/helpers/aitable.go:7235
visible_flags: 6

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --role-id <String>: 目标自定义角色 ID (必填，系统角色禁止更新)
- --name <String>: 新角色名称 (可选，不传不修改)
- --role-type <String>: 角色类型 (可选)
- --flow-type <String>: 流程类型 (可选)
- --sub-roles <String>: 子角色配置 JSON 数组，PATCH 语义：按 (targetId,targetType) 合并入现有 subRoles，未提及的 sub 保留

## Related
- dws aitable advperm disable
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
