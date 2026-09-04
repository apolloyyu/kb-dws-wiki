# dws aitable advperm disable

kind: command
completeness: full
usage: dws aitable advperm disable
description: 关闭高级权限总开关（高危）
example: dws aitable advperm disable --base-id BASE_ID --yes
source: internal/helpers/aitable.go:7056
visible_flags: 1

## Flags
- --base-id <String>: 目标 Base ID (必填)

## Related
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
