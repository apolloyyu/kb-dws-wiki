# dws todo +todo-done

kind: shortcut
completeness: full
usage: dws todo +todo-done
description: 按标题关键词把我的某条待办标记完成（自动定位 taskId）
source: internal/shortcut/smart/todo_done.go:48
visible_flags: 1

## Flags
- --task <String>: 待办标题关键词

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
