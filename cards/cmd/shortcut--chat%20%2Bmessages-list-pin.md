# dws chat +messages-list-pin

kind: shortcut
completeness: full
usage: dws chat +messages-list-pin
description: 拉取会话中钉住的消息列表
source: internal/shortcut/chat/chat_message.go:2282
visible_flags: 3

## Flags
- --open-conversation-id <String>: 会话 openConversationId
- --cursor <String>: 分页游标，翻页传 nextCursor
- --size <Int>: 一次拉取的消息数量（默认 20，最大 100）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
