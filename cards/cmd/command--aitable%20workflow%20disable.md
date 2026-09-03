# dws aitable workflow disable

kind: command
completeness: full
description: 禁用指定工作流（高危）
source: internal/helpers/aitable.go:5900
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws aitable workflow create
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow get
- dws aitable workflow history
- dws aitable workflow list
