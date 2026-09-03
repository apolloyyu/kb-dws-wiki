# dws todo task list-sub

kind: command
completeness: full
usage: dws todo task list-sub
description: 查询子待办列表
example: dws todo task list-sub --task-id <taskId>
source: internal/helpers/todo.go:347
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
