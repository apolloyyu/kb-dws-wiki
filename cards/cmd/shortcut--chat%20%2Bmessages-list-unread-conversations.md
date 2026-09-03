# dws chat +messages-list-unread-conversations

kind: shortcut
completeness: full
usage: dws chat +messages-list-unread-conversations
description: 获取有未读消息的会话列表
source: internal/shortcut/chat/chat_message.go:713
visible_flags: 2

## Flags
- --count <Int>: 返回的会话条数
- --exclude-muted <Bool>: 排除已免打扰会话

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
