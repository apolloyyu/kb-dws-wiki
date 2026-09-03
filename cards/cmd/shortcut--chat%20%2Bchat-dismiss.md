# dws chat +chat-dismiss

kind: shortcut
completeness: full
usage: dws chat +chat-dismiss
description: 解散群聊（不可逆，需群主权限）
source: internal/shortcut/chat/chat_group.go:580
visible_flags: 1

## Flags
- --group <String>: 群 openConversationId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
