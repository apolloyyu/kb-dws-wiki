# dws aitable advperm role-delete

kind: command
completeness: full
description: 删除自定义角色（不可逆）
source: internal/helpers/aitable.go:7302
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --role-id <String>: 目标自定义角色 ID（系统角色禁删） (必填)

## Related
- dws aitable advperm disable
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
