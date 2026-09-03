# dws todo task add-reminder

kind: command
completeness: full
description: 添加待办提醒
source: internal/helpers/todo.go:877
visible_flags: 4

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --base-time <String>: 提醒基准时间: dueTime/customTime (必填)
- --due-date-offset <String>: 截止时间偏移量，为整数 (baseTime=dueTime 时必填)
- --reminder-time-stamp <String>: 自定义提醒时间 ISO-8601 (如 2026-03-10T18:00:00+08:00，baseTime=customTime 时必填)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task create
- dws todo task create-sub
- dws todo task delete
