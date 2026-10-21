# dws todo +assign

kind: shortcut
completeness: full
usage: dws todo +assign
description: 按姓名给某人创建并指派一条待办（自动解析 userId）
source: internal/shortcut/smart/assign.go:37
visible_flags: 3

## Flags
- --to <String>: 执行人姓名/花名
- --task <String>: 待办标题/内容
- --due <String>: 截止时间（ISO8601，可选）

## Related
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
- dws todo +get
