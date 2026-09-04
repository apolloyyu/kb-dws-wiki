# dws chat mark-read

kind: command
completeness: full
usage: dws chat mark-read
description: 标记消息已读
example: dws chat mark-read --conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat.go:10088
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)
- --message-id <String> required: 消息 openMessageId (必填)

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
