# dws chat hide

kind: command
completeness: full
usage: dws chat hide
description: 会话列表中隐藏会话
example: dws chat hide --conversation-id <openConversationId>
source: internal/helpers/chat.go:10393
visible_flags: 1

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
