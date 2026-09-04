# dws aitable workflow enable

kind: command
completeness: full
usage: dws aitable workflow enable
description: 启用指定工作流
example: dws aitable workflow enable --base-id BASE_ID --workflow-id WORKFLOW_ID
source: internal/helpers/aitable.go:5869
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
