# dws todo tag delete

kind: command
completeness: full
description: 删除待办
source: internal/helpers/todo.go:592
visible_flags: 1

## Flags
- --task-id <String>: 待办任务 ID (必填)

## Related
- dws todo tag add
- dws todo tag create
- dws todo tag list
- dws todo tag update
