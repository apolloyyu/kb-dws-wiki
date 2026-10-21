# dws todo +due-today

kind: shortcut
completeness: full
usage: dws todo +due-today
description: 列出我今天到期的待办
source: internal/shortcut/smart/due_today.go:53
visible_flags: 1

## Flags
- --role-types <String>: 覆盖默认角色范围，逗号分隔，取值 creator/executor/participant；不传则默认 executor

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +get
