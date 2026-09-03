# dws smart +my-groups

kind: shortcut
completeness: full
usage: dws smart +my-groups
description: 列出我加入的群，可按类型过滤并投影关键字段
source: internal/shortcut/smart/my_groups.go:52
visible_flags: 5

## Flags
- --type <String>: 按群类型过滤（可选，如返回中的 groupType/conversationType，大小写不敏感）
- --limit <Int>: 每页返回数量（默认 200）；--limit 必须在 1-200 之间
- --cursor <String>: 分页游标，翻页传上次的 nextCursor
- --page-all <Bool>: 沿 nextCursor 自动读取全部已加入群；--page-limit 仅与 --page-all 一起使用且范围 1-500；--max-items/--page-delay 仅与 --page-all 一起使用；值必须大于等于 0
- --page-limit <Int>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
