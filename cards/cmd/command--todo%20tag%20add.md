# dws todo tag add

kind: command
completeness: full
description: 新增待办评论
source: internal/helpers/todo.go:1314
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --content <String>: 评论内容 (必填)

## Related
- dws todo tag create
- dws todo tag delete
- dws todo tag list
- dws todo tag update
