# dws todo task list-attachment

kind: command
completeness: full
usage: dws todo task list-attachment
description: 查询待办任务的附件列表
example: dws todo task list-attachment --task-id <taskId>
source: internal/helpers/todo.go:1135
visible_flags: 1

## Flags
- --task-id <String>: 待办任务 ID (必填)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
