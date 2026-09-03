# dws smart +thread-replies

kind: shortcut
completeness: full
usage: dws smart +thread-replies
description: 按主消息 ID 或 thread/topic ID 分页读取话题回复，支持完整排序与有界自动翻页
source: internal/shortcut/smart/thread_replies.go:54
visible_flags: 12

## Flags
- --group <String>: 群会话 ID；--thread-id/--topic-id 必须同时提供 --group；--group 与 --message-id 解析出的 conversationId 必须匹配
- --message-id <String>: 话题主消息 openMessageId；自动只读解析 conversationId 和 threadId；--group 与 --message-id 解析出的 conversationId 必须匹配
- --thread-id <String>: 话题/线程 ID（可直接使用消息列表返回的 threadId）；--thread-id/--topic-id 必须同时提供 --group
- --topic-id <String>: --thread-id 的兼容别名；--thread-id/--topic-id 必须同时提供 --group
- --time <String>: 起始时间，如 \"2025-03-01 00:00:00\"；--time 必须是 RFC3339、YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD（可选）
- --limit <Int>: 每页拉取的回复条数；--limit 必须大于 0
- --page-size <Int>: --limit 的公开兼容别名；必须大于 0
- --page-all <Bool>: 沿下层毫秒级 nextCursor 自动读取后续页；--page-limit 仅与 --page-all 一起使用且范围 1-500；asc 必须与 --page-all 一起使用
- --page-limit <Int>: —
- --order <String>: —
- --sort <String>: —
- --no-reactions <Bool>: 不输出回复 reaction（默认输出）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
