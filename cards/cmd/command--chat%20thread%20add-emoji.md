# dws chat thread add-emoji

kind: command
completeness: full
description: Add an emoji reaction to a Thread message.
use_when: When the agent needs to react to a Thread root or reply.
source: internal/helpers/chat.go:6248
visible_flags: 7

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --group <String>: --conversation-id 的别名
- --id <String>: --conversation-id 的别名
- --chat <String>: --conversation-id 的别名
- --open-conversation-id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMsgId (必填)
- --emoji <String>: emoji 表情名称 (必填)

## Related
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
