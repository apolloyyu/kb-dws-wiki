# dws chat +conversation-mark-read

kind: shortcut
completeness: full
usage: dws chat +conversation-mark-read
description: 标记消息已读（该消息及之前的消息都标记为已读）
source: internal/shortcut/chat/chat_conversation.go:985
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId
- --message-id <String>: 消息 openMessageId

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
