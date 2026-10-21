# dws chat +chat-update

kind: shortcut
completeness: full
usage: dws chat +chat-update
description: 更新群名称（仅名称，不支持 description）
source: internal/shortcut/chat/lark_alignment.go:187
visible_flags: 2

## Flags
- --group <String>: 群名称或 openConversationId
- --name <String>: 新的群名称

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
