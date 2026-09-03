# dws todo task update

kind: command
completeness: full
description: Update a todo's title, description, due time, or executors.
use_when: When the agent edits an existing todo after new information comes in.
source: internal/helpers/todo.go:366
visible_flags: 5

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --title <String>: 新标题
- --due <String>: 截止时间 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --priority <String>: 优先级: 10低/20普通/30较高/40紧急
- --done <String>: 完成状态: true/false

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
