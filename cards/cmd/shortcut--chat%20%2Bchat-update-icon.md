# dws chat +chat-update-icon

kind: shortcut
completeness: full
usage: dws chat +chat-update-icon
description: 更新群头像
source: internal/shortcut/chat/chat_group.go:536
visible_flags: 2

## Flags
- --group <String>: 群 openConversationId
- --icon-media-id <String>: 群头像 mediaId（以 @ 开头）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
