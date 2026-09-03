# dws smart +assign-multi

kind: shortcut
completeness: full
description: 把一条待办按姓名一次性指派给多个人（自动把每个姓名解析成 userId）
source: internal/shortcut/smart/assign_multi.go:49
visible_flags: 2

## Flags
- --to <StringSlice>: 执行人姓名/花名，逗号分隔（如 张三,李四）
- --task <String>: 待办标题

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +at-me
