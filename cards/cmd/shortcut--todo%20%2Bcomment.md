# dws todo +comment

kind: shortcut
completeness: full
usage: dws todo +comment
description: 添加待办评论并读回验证
source: internal/shortcut/todo/lifecycle.go:332
visible_flags: 2

## Flags
- --task-id <String>: 待办 taskId
- --content <String>: 评论内容

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
- dws todo +get
