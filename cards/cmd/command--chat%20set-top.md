# dws chat set-top

kind: command
completeness: full
usage: dws chat set-top
description: 会话置顶 / 取消置顶（支持单聊/群聊）
example: dws chat set-top --conversation-id <openConversationId>
source: internal/helpers/chat.go:7774
visible_flags: 2

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填，支持单聊/群聊)
- --off <Bool>: 取消置顶（不传则设置置顶）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
