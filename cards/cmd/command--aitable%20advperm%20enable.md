# dws aitable advperm enable

kind: command
completeness: full
usage: dws aitable advperm enable
description: 开启高级权限总开关
example: dws aitable advperm enable --base-id BASE_ID
source: internal/helpers/aitable.go:7017
visible_flags: 1

## Flags
- --base-id <String>: 目标 Base ID (必填)

## Related
- dws aitable advperm disable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
