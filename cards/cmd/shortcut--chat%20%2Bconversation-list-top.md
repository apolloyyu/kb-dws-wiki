# dws chat +conversation-list-top

kind: shortcut
completeness: full
usage: dws chat +conversation-list-top
description: 拉取置顶会话列表，可只看群聊或单聊
source: internal/shortcut/chat/chat_conversation.go:579
visible_flags: 4

## Flags
- --limit <Int>: 每页数量
- --cursor <Int>: 分页游标（首次不传或 0）
- --exclude-muted <Bool>: 排除已免打扰会话
- --type <String>: —

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
