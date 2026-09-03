# dws chat +messages-list

kind: shortcut
completeness: full
description: 拉取群聊会话消息
source: internal/shortcut/chat/chat_message.go:289
visible_flags: 8

## Flags
- --group <String>: 群 openConversationId
- --conversation-id <String>: --group 的别名
- --id <String>: --group 的别名
- --time <String>: 起始时间，如 \"2025-03-01 00:00:00\"
- --forward <Bool>: —
- --limit <Int>: 每页返回数量；显式页大小必须大于 0
- --size <Int>: --limit 的旧版别名；显式页大小必须大于 0
- --no-reactions <Bool>: 不输出消息 reaction（默认输出）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
