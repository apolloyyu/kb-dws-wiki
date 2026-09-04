# dws aitable workflow disable

kind: command
completeness: full
usage: dws aitable workflow disable
description: 禁用指定工作流（高危）
example: dws aitable workflow disable --base-id BASE_ID --workflow-id WORKFLOW_ID --yes
source: internal/helpers/aitable.go:5912
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
