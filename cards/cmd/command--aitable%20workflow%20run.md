# dws aitable workflow run

kind: command
completeness: partial
usage: dws aitable workflow run
description: —
source: internal/helpers/aitable.go:7530
visible_flags: 4
partial_reason: missing_description

## Flags
- --base-id <String> required: 目标 Base ID (必填)
- --workflow-id <String> required: 目标工作流 ID (必填)
- --table-id <String>: 记录类触发器绑定的 Table ID；定时触发器不传
- --record-ids <StringSlice>: 触发工作流的记录 ID，逗号分隔；记录类触发器必填，1 到 5 个且不可重复

## Related
- dws aitable workflow create
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow get
- dws aitable workflow history
