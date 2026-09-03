# dws aitable workflow enable

kind: command
completeness: full
description: 启用指定工作流
source: internal/helpers/aitable.go:5857
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws aitable workflow create
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow get
- dws aitable workflow history
- dws aitable workflow list
