# dws todo +update

kind: shortcut
completeness: full
usage: dws todo +update
description: 更新待办并读回验证
source: internal/shortcut/todo/lifecycle.go:221
visible_flags: 4

## Flags
- --task-id <String>: 待办 taskId
- --title <String>: 新标题
- --due <String>: 新截止时间（ISO8601）
- --priority <Int>: 新优先级；--priority 仅接受 10/20/30/40

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
