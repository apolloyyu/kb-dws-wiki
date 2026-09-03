# dws chat +chat-update-alias

kind: shortcut
completeness: full
usage: dws chat +chat-update-alias
description: 设置群备注（仅自己可见）
source: internal/shortcut/chat/chat_group.go:714
visible_flags: 2

## Flags
- --group <String>: 群 openConversationId
- --alias-title <String>: 群备注标题

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
