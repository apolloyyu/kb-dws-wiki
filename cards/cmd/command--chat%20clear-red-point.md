# dws chat clear-red-point

kind: command
completeness: full
usage: dws chat clear-red-point
description: 清除会话红点
example: dws chat clear-red-point --conversation-id <openConversationId>
source: internal/helpers/chat.go:9654
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持群聊/单聊)

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat conversation-file
