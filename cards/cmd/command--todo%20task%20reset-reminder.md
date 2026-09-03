# dws todo task reset-reminder

kind: command
completeness: full
description: 重置待办提醒
source: internal/helpers/todo.go:967
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --reminder-rules <String>: 提醒规则 JSON 数组 (不传则清除；显式传值必须合法)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
