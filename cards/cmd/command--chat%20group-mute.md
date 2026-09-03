# dws chat group-mute

kind: command
completeness: full
description: 全员禁言 / 取消全员禁言
source: internal/helpers/chat.go:7883
visible_flags: 2

## Flags
- --conversation-id <String>: 群聊 openConversationId (必填)
- --off <Bool>: 取消全员禁言（不传则开启禁言）

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
