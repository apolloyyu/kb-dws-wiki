# dws chat +category-list-conversations

kind: shortcut
completeness: full
usage: dws chat +category-list-conversations
description: 按稳定 categoryId 列出会话分组中的会话
source: internal/shortcut/chat/chat_conversation.go:963
visible_flags: 2

## Flags
- --category-id <Int>: 稳定会话分组 ID
- --exclude-muted <Bool>: 排除已免打扰会话

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
