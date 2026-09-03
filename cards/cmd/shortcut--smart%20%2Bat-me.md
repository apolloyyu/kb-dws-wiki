# dws smart +at-me

kind: shortcut
completeness: full
usage: dws smart +at-me
description: 查最近 @我 的消息（自动算时间窗，投影发送人/时间/内容/会话）
source: internal/shortcut/smart/at_me.go:60
visible_flags: 9

## Flags
- --group <String>: 仅查看指定群；可传 openConversationId 或群名
- --chat-query <String>: --group 的旧版自然名称入口
- --group-query <String>: --chat-query 的兼容别名
- --days <Int>: 回溯天数（默认 7）；--days 必须在 1-3650 之间
- --limit <Int>: 每页返回数量（默认 50）；--limit 必须大于 0
- --cursor <String>: 分页游标，翻页传上次的 nextCursor
- --page-all <Bool>: 沿 nextCursor 自动读取全部 @我 消息；--page-limit 仅与 --page-all 一起使用且范围 1-500；--max-items/--page-delay 仅与 --page-all 一起使用；值必须大于等于 0
- --page-limit <Int>: —
- --no-reactions <Bool>: 不输出消息 reaction（默认输出）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
