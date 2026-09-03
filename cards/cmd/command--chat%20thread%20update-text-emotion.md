# dws chat thread update-text-emotion

kind: command
completeness: full
description: Atomically replace a text emotion on a Thread message.
use_when: When the agent needs to change a Thread message status.
source: internal/helpers/chat.go:6532
visible_flags: 8

## Flags
- --conversation-id <String> required: 会话 openConversationId (必填，支持单聊/群聊)
- --open-conversation-id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMsgId (必填)
- --old-emotion-id <String>: 待更新的原表情 ID (必填)
- --emotion-id <String>: 新表情 ID (必填)
- --emotion-name <String>: 新表情名称 (必填)
- --text <String>: 新文字内容 (必填)
- --background-id <String>: 新背景 ID (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
