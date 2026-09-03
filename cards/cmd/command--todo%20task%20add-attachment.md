# dws todo task add-attachment

kind: command
completeness: partial
usage: dws todo task add-attachment
description: 上传待办附件
example: dws todo task add-attachment --task-id <taskId> --file <filePath>
source: internal/helpers/todo.go:1039
visible_flags: 1
partial_reason: unverified_flags

## Flags
- --task-id <String>: 待办任务 ID (必填)

## Related
- dws todo task add-executor
- dws todo task add-participant
- dws todo task add-reminder
- dws todo task create
- dws todo task create-sub
- dws todo task delete
