# dws chat +conversation-mute-red-envelope

kind: shortcut
completeness: full
usage: dws chat +conversation-mute-red-envelope
description: 关闭/开启红包消息提醒
source: internal/shortcut/chat/chat_conversation.go:190
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId
- --off <Bool>: 恢复接收红包通知（不传则关闭通知）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
