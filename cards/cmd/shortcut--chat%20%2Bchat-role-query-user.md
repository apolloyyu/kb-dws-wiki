# dws chat +chat-role-query-user

kind: shortcut
completeness: full
usage: dws chat +chat-role-query-user
description: 查询群成员的群身份
source: internal/shortcut/chat/chat_group.go:1965
visible_flags: 2

## Flags
- --group <String>: 群 openConversationId
- --user <String>: 用户 userId 或 openDingTalkId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
