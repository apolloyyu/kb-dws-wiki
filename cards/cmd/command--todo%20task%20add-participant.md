# dws todo task add-participant

kind: command
completeness: full
usage: dws todo task add-participant
description: 添加待办参与人
example: dws todo task add-participant --task-id <taskId> --participants <USER_ID_1>,<USER_ID_2>
source: internal/helpers/todo.go:761
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --participants <String>: 参与人 userId 列表 (必填)

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
- dws todo task delete
