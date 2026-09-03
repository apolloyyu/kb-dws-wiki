# dws chat conversation-info

kind: command
completeness: full
description: Retrieve basic metadata for a conversation (single chat or group chat) by conversation ID.
use_when: When the agent needs context about a conversation (name, type, member count) before operating on it.
source: internal/helpers/chat.go:5479
visible_flags: 3

## Flags
- --conversation-id <String>: 群聊 openConversationId（群聊时使用）
- --user <String>: 单聊对方 userId（单聊时使用）
- --open-dingtalk-id <String>: 单聊对方 openDingTalkId（单聊时使用）

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat emotion
- dws chat group-mute
