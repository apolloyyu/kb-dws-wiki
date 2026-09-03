# dws aitable advperm role-create

kind: command
completeness: full
description: 创建自定义角色
source: internal/helpers/aitable.go:7171
visible_flags: 5

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --name <String>: 角色名称 (必填)
- --role-type <String>: 角色类型 (留空由下游决定默认值，如 custom)
- --flow-type <String>: 流程类型 (按业务需要填写，留空表示无流程绑定)
- --sub-roles <String>: 子角色配置 JSON 数组：[{targetId,targetType,authLevel,appId?,config?}]

## Related
- dws aitable advperm disable
- dws aitable advperm enable
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
