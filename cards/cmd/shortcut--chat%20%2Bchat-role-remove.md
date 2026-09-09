# dws chat +chat-role-remove

kind: shortcut
completeness: full
usage: dws chat +chat-role-remove
description: 删除群身份
source: internal/shortcut/chat/chat_group.go:1873
visible_flags: 2

## Flags
- --group <String>: 群名或 openConversationId；群名必须唯一匹配
- --role-id <String>: 群身份 openRoleId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
