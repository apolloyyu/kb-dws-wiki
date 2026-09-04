# dws aitable advperm role-delete

kind: command
completeness: full
usage: dws aitable advperm role-delete
description: 删除自定义角色（不可逆）
example: dws aitable advperm role-delete --base-id BASE_ID --role-id ROLE_ID --yes
source: internal/helpers/aitable.go:7314
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
