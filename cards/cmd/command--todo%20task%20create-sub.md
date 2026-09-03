# dws todo task create-sub

kind: command
completeness: full
usage: dws todo task create-sub
description: 创建子待办
example: dws todo task create-sub --parent-id <parentId> --title "子任务标题" --executors userId1,userId2 --priority 40
source: internal/helpers/todo.go:176
visible_flags: 6

## Flags
- --parent-id <String>: 父待办任务 ID (必填)
- --title <String>: 子待办标题 (必填)
- --executors <String>: 执行者 userId 列表，逗号分隔且至少一个非空值 (必填)
- --due <String>: 截止时间 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --priority <String>: 优先级: 10低/20普通/30较高/40紧急
- --recurrence <String>: 循环待办 (需先设置 --due); 格式: DTSTART:20260320T100000Z\\nRRULE:FREQ=DAILY;INTERVAL=1

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task delete
