# dws chat mute-red-envelope

kind: command
completeness: full
usage: dws chat mute-red-envelope
description: 关闭/开启红包消息提醒
example: dws chat mute-red-envelope --conversation-id <openConversationId>
source: internal/helpers/chat.go:10512
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --off <Bool>: 恢复接收红包通知（不传则关闭通知）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
