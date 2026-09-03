# dws chat +chat-transfer-owner

kind: shortcut
completeness: full
usage: dws chat +chat-transfer-owner
description: 转让群主
source: internal/shortcut/chat/chat_group.go:429
visible_flags: 2

## Flags
- --group <String>: 群 openConversationId
- --new-owner <String>: 新群主 userId 或 openDingTalkId

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
