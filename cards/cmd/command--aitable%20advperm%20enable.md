# dws aitable advperm enable

kind: command
completeness: full
description: 启用指定工作流
source: internal/helpers/aitable.go:5857
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws aitable advperm disable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
