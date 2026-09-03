# dws chat +category-add-conversation

kind: shortcut
completeness: full
description: 将会话移动到指定的自定义分组中
source: internal/shortcut/chat/chat_conversation.go:1196
visible_flags: 2

## Flags
- --group <String>: 会话 openConversationId
- --category-ids <StringSlice>: 目标分组 ID 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
- dws chat +category-list-conversations
