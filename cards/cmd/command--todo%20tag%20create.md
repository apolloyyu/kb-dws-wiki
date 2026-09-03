# dws todo tag create

kind: command
completeness: full
description: 创建待办
source: internal/helpers/todo.go:87
visible_flags: 5

## Flags
- --title <String>: 待办标题 (必填)
- --executors <String>: 执行者 userId 列表，逗号分隔且至少一个非空值 (必填)
- --due <String>: 截止时间 ISO-8601 (如 2026-03-10T18:00:00+08:00)
- --priority <String>: 优先级: 10低/20普通/30较高/40紧急
- --recurrence <String>: 循环待办 (需先设置 --due); 格式: DTSTART:20260320T100000Z\\nRRULE:FREQ=DAILY;INTERVAL=1

## Related
- dws todo tag add
- dws todo tag delete
- dws todo tag list
- dws todo tag update
