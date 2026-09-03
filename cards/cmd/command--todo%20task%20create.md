# dws todo task create

kind: command
completeness: full
description: Create a personal todo item for the current user with title, due time, and optional executors.
use_when: When the agent captures an action item as a tracked todo in the user's DingTalk todo list.
source: internal/helpers/todo.go:87
visible_flags: 5

## Flags
- --title <String>: 待办标题 (必填)
- --executors <String>: 执行者 userId 列表，逗号分隔且至少一个非空值 (必填)
- --due <String>: 截止时间 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --priority <String>: 优先级: 10低/20普通/30较高/40紧急
- --recurrence <String>: 循环待办 (需先设置 --due); 格式: DTSTART:20260320T100000Z\\nRRULE:FREQ=DAILY;INTERVAL=1

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create-sub
- dws todo task delete
