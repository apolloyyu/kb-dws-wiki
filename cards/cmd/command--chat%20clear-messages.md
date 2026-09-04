# dws chat clear-messages

kind: command
completeness: full
usage: dws chat clear-messages
description: 清空当前用户指定会话的聊天记录
example: dws chat clear-messages --conversation-id <openConversationId>
source: internal/helpers/chat.go:10020
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-red-point
- dws chat conversation-file
