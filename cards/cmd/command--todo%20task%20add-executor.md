# dws todo task add-executor

kind: command
completeness: full
description: 添加待办执行人
source: internal/helpers/todo.go:640
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --executors <String>: 执行者 userId 列表，逗号分隔且至少一个非空值 (必填)

## Related
- dws todo task add-attachment
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
- dws todo task delete
