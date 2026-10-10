# dws aitable workflow history

kind: command
completeness: partial
usage: dws aitable workflow history
description: —
source: internal/helpers/aitable.go:7584
visible_flags: 7
partial_reason: missing_description

## Flags
- --base-id <String> required: 目标 Base ID (必填)
- --workflow-id <String> required: 目标工作流 ID (必填)
- --status <String>: 执行状态筛选；不传表示全部(可选: success|failed|running|break|untrigger)
- --after-time <Int>: 开始时间（Unix 毫秒）
- --before-time <Int>: 结束时间（Unix 毫秒）
- --page <Int>: 页码，从 0 开始
- --size <Int>: 每页条数 [1, 100]

## Related
- dws aitable workflow create
- dws aitable workflow disable
- dws aitable workflow edit-example
- dws aitable workflow enable
- dws aitable workflow get
- dws aitable workflow list
