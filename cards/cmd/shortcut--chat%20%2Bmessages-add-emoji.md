# dws chat +messages-add-emoji

kind: shortcut
completeness: full
usage: dws chat +messages-add-emoji
description: 对消息添加 emoji 表情回应
source: internal/shortcut/chat/chat_message.go:1332
visible_flags: 3

## Flags
- --conversation-id <String>: 会话 openConversationId
- --msg-id <String>: 消息 openMsgId
- --emoji <String>: emoji 表情名称

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
