# dws chat +messages-forward

kind: shortcut
completeness: full
usage: dws chat +messages-forward
description: 转发单条消息
source: internal/shortcut/chat/chat_message.go:1892
visible_flags: 4

## Flags
- --src-conversation-id <String>: 源会话 openConversationId
- --msg-id <String>: 源消息 openMessageId
- --dest-conversation-id <String>: 目标会话 openConversationId
- --uuid <String>: 幂等键（可选）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
