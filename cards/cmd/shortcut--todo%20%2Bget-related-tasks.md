# dws todo +get-related-tasks

kind: shortcut
completeness: full
usage: dws todo +get-related-tasks
description: 一次性列出与我相关的全部待办（我作为创建人/执行人/参与人三种角色的并集，按 taskId 去重）
source: internal/shortcut/smart/related_tasks.go:55
visible_flags: 2

## Flags
- --role-types <String>: 覆盖默认角色范围，逗号分隔，取值 creator/executor/participant；不传则默认三者并集
- --status <String>: 按 todoStatus 过滤（透传给 get_user_todos_in_current_org）

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
