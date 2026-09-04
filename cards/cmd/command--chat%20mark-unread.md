# dws chat mark-unread

kind: command
completeness: full
usage: dws chat mark-unread
description: 标记会话为未读
example: dws chat mark-unread --conversation-id <openConversationId>
source: internal/helpers/chat.go:9796
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
