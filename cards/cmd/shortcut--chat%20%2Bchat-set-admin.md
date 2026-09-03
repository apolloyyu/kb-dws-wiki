# dws chat +chat-set-admin

kind: shortcut
completeness: full
usage: dws chat +chat-set-admin
description: 设置 / 取消群管理员
source: internal/shortcut/chat/chat_group.go:1420
visible_flags: 3

## Flags
- --group <String>: 群 openConversationId
- --users <StringSlice>: 成员 userId 或 openDingTalkId 列表
- --off <Bool>: 取消管理员（不传则设为管理员）

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
