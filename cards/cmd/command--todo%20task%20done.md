# dws todo task done

kind: command
completeness: full
usage: dws todo task done
description: Update the completion status of a todo's executor (mark done or undone).
example: dws todo task done --task-id <taskId> --status true
use_when: When the agent marks an action item as completed after confirming the work is finished.
source: internal/helpers/todo.go:450
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --status <String>: 完成状态: true=已完成, false=未完成 (必填)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
