# dws chat group-mute

kind: command
completeness: full
usage: dws chat group-mute
description: 全员禁言 / 取消全员禁言
example: dws chat group-mute --conversation-id <openConversationId>
source: internal/helpers/chat.go:7883
visible_flags: 2

## Flags
- --conversation-id <String>: 群聊 openConversationId (必填)
- --off <Bool>: 取消全员禁言（不传则开启禁言）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
