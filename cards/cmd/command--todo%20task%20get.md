# dws todo task get

kind: command
completeness: full
usage: dws todo task get
description: Retrieve the full details of a todo item by ID.
example: dws todo task get --task-id <taskId>
use_when: When the agent inspects a specific todo's content, due date, and executors.
source: internal/helpers/todo.go:511
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
