# dws todo task delete

kind: command
completeness: full
description: Delete a todo item by ID.
use_when: When the agent removes a todo that is no longer relevant.
source: internal/helpers/todo.go:592
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
