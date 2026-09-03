# dws chat mark-unread

kind: command
completeness: full
description: 标记会话为未读
source: internal/helpers/chat.go:9594
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
