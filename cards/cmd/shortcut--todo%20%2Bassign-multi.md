# dws todo +assign-multi

kind: shortcut
completeness: full
usage: dws todo +assign-multi
description: 把一条待办按姓名一次性指派给多个人（自动把每个姓名解析成 userId）
source: internal/shortcut/smart/assign_multi.go:49
visible_flags: 2

## Flags
- --to <StringSlice>: 执行人姓名/花名，逗号分隔（如 张三,李四）
- --task <String>: 待办标题

## Related
- dws todo +assign
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
- dws todo +get
