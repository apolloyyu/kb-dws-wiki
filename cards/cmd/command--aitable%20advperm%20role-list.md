# dws aitable advperm role-list

kind: command
completeness: full
usage: dws aitable advperm role-list
description: 列出 Base 下所有角色
example: dws aitable advperm role-list --base-id BASE_ID
source: internal/helpers/aitable.go:7089
visible_flags: 1

## Flags
- --base-id <String>: 目标 Base ID (必填)

## Related
- dws aitable advperm disable
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-update
