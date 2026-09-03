# dws aitable advperm disable

kind: command
completeness: full
description: 禁用指定工作流（高危）
source: internal/helpers/aitable.go:5900
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws aitable advperm enable
- dws aitable advperm role-create
- dws aitable advperm role-delete
- dws aitable advperm role-get
- dws aitable advperm role-list
- dws aitable advperm role-update
