# dws chat +send-to-group

kind: shortcut
completeness: full
usage: dws chat +send-to-group
description: 按群名或 openConversationId 直接给群发消息
source: internal/shortcut/smart/send_to_group.go:39
visible_flags: 2

## Flags
- --group <String>: 群名称或 openConversationId
- --content <String>: 消息内容（支持 Markdown）

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
