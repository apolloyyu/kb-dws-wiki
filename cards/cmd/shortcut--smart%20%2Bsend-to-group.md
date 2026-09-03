# dws smart +send-to-group

kind: shortcut
completeness: full
description: 按群名或 openConversationId 直接给群发消息
source: internal/shortcut/smart/send_to_group.go:39
visible_flags: 2

## Flags
- --group <String>: 群名称或 openConversationId
- --content <String>: 消息内容（支持 Markdown）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
