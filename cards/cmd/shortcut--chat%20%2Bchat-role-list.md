# dws chat +chat-role-list

kind: shortcut
completeness: full
usage: dws chat +chat-role-list
description: 拉取会话的群身份列表
source: internal/shortcut/chat/chat_group.go:1693
visible_flags: 1

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
