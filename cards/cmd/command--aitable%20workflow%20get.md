# dws aitable workflow get

kind: command
completeness: full
usage: dws aitable workflow get
description: 获取单个工作流详情
example: dws aitable workflow get --base-id BASE_ID --workflow-id WORKFLOW_ID
source: internal/helpers/aitable.go:5960
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws aitable workflow create
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow history
- dws aitable workflow list
