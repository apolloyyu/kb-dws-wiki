# dws chat +conversation-mute

kind: shortcut
completeness: full
usage: dws chat +conversation-mute
description: 会话消息免打扰（支持单聊/群聊）
source: internal/shortcut/chat/chat_conversation.go:147
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId
- --off <Bool>: 关闭免打扰（不传则开启免打扰）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
