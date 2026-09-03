# dws chat +conversation-clear-messages

kind: shortcut
completeness: full
description: 清空当前用户指定会话的聊天记录（仅本人视角，不可逆）
source: internal/shortcut/chat/chat_conversation.go:776
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
