# dws chat +chat-role-add

kind: shortcut
completeness: full
usage: dws chat +chat-role-add
description: 添加群身份
source: internal/shortcut/chat/chat_group.go:1771
visible_flags: 2

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配
- --name <String>: 群身份名称

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
