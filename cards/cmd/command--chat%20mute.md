# dws chat mute

kind: command
completeness: full
description: 会话消息免打扰
source: internal/helpers/chat.go:7329
visible_flags: 4

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --id <String>: --conversation-id 的别名
- --chat <String>: --conversation-id 的别名
- --off <Bool>: 关闭免打扰（不传则开启免打扰）

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
