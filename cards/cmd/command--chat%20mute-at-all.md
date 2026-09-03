# dws chat mute-at-all

kind: command
completeness: full
usage: dws chat mute-at-all
description: 关闭/开启 @所有人消息提醒
example: dws chat mute-at-all --conversation-id <openConversationId>
source: internal/helpers/chat.go:10249
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --off <Bool>: 恢复接收 @所有人通知（不传则关闭通知）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
