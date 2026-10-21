# dws chat +category-add-conversation

kind: shortcut
completeness: full
usage: dws chat +category-add-conversation
description: 将会话移动到指定的自定义分组中
source: internal/shortcut/chat/chat_conversation.go:1611
visible_flags: 2

## Flags
- --group <String>: 会话 openConversationId
- --category-ids <StringSlice>: 目标分组 ID 列表

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-create
- dws chat +category-delete
