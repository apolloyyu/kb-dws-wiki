# dws aitable advperm role-get

kind: command
completeness: full
description: 获取单个角色完整配置
source: internal/helpers/aitable.go:7130
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --role-id <String>: 目标角色 ID (字符串形态的 long 数字) (必填)

## Related
- dws aitable advperm disable
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-list
- dws aitable advperm role-update
