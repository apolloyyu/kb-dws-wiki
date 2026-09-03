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
- dws todo +create
- dws todo +get
- dws todo +get-my-tasks
- dws todo +list-attachment
- dws todo +list-comment
- dws todo +list-sub
