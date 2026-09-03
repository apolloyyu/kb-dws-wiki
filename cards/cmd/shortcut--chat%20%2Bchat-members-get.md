# dws chat +chat-members-get

kind: shortcut
completeness: full
description: 根据成员 openDingTalkId 批量查询群成员详情
source: internal/shortcut/chat/chat_group.go:401
visible_flags: 2

## Flags
- --id <String>: 群 openConversationId
- --users <StringSlice>: 成员 openDingTalkId 列表

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
