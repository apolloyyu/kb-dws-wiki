# dws chat +category-remove-conversation

kind: shortcut
completeness: full
usage: dws chat +category-remove-conversation
description: 将会话从指定的自定义分组中移出
source: internal/shortcut/chat/chat_conversation.go:1221
visible_flags: 2

## Flags
- --group <String>: 会话 openConversationId
- --category-ids <StringSlice>: 目标分组 ID 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
