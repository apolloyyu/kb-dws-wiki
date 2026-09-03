# dws chat mark-read

kind: command
completeness: full
description: 标记消息已读
source: internal/helpers/chat.go:9886
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)
- --message-id <String> required: 消息 openMessageId (必填)

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
