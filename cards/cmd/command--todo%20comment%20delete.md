# dws todo comment delete

kind: command
completeness: full
usage: dws todo comment delete
description: 删除待办评论
example: dws todo comment delete --task-id <taskId> --comment-id <commentId>
source: internal/helpers/todo.go:1419
visible_flags: 2

## Flags
- --task-id <String>: 待办任务 ID (必填)
- --comment-id <String>: 评论 ID (必填)

## Related
- dws todo comment add
- dws todo comment list
