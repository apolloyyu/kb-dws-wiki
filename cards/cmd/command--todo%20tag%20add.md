# dws todo tag add

kind: command
completeness: full
usage: dws todo tag add
description: 给待办打标
example: dws todo tag add --task-id <taskId> --tag-codes code1,code2
source: internal/helpers/todo.go:1485
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --tag-codes <String>: 标签编码列表，逗号分隔 (必填)

## Related
- dws todo tag create
- dws todo tag delete
- dws todo tag list
- dws todo tag update
