# dws chat +chat-role-update

kind: shortcut
completeness: full
usage: dws chat +chat-role-update
description: 更新群身份名称
source: internal/shortcut/chat/chat_group.go:1821
visible_flags: 3

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配
- --role-id <String>: 群身份 openRoleId
- --name <String>: 群身份新名称

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
