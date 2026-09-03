# dws todo task remove-participant

kind: command
completeness: full
description: 移除待办参与人
source: internal/helpers/todo.go:819
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --participants <String>: 参与人 userId 列表 (必填)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
