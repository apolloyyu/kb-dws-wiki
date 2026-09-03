# dws chat thread add-text-emotion

kind: command
completeness: full
description: Add a text emotion to a Thread message.
use_when: When the agent needs to attach a known text status such as processing or resolved.
source: internal/helpers/chat.go:6386
visible_flags: 10

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --group <String>: --conversation-id 的别名
- --id <String>: --conversation-id 的别名
- --chat <String>: --conversation-id 的别名
- --open-conversation-id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMsgId (必填)
- --emotion-id <String>: 表情 ID (必填，通过 create-text-emotion 获取)
- --emotion-name <String>: 表情名称 (必填)
- --text <String>: 文字内容 (必填)
- --background-id <String>: 背景 ID (必填)

## Related
- dws chat thread add-emoji
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
