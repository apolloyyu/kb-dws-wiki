# dws todo task remove-attachment

kind: command
completeness: full
usage: dws todo task remove-attachment
description: 删除待办任务的附件
example: dws todo task remove-attachment --task-id <taskId> --attachment-id <attachmentId>
source: internal/helpers/todo.go:1191
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --attachment-id <String>: 待办附件 ID（必填）

## Related
- dws todo task add-attachment
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
