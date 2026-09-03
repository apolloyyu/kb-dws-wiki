# dws todo comment list

kind: command
completeness: full
usage: dws todo comment list
description: 查询待办评论列表
example: dws todo comment list --task-id <taskId>
source: internal/helpers/todo.go:1364
visible_flags: 3

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --page <String>: 页码 (默认 1)
- --size <String>: 每页数量 (默认 20)

## Related
- dws todo comment add
- dws todo comment delete
