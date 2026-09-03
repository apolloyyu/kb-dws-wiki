# dws chat message remove-text-emotion

kind: command
completeness: full
description: 移除消息的文字表情回应
source: internal/helpers/chat.go:6459
visible_flags: 10

## Flags
- --conversation-id <String>: 会话 openConversationId (必填，支持单聊/群聊)
- --group <String>: --conversation-id 的别名
- --id <String>: --conversation-id 的别名
- --chat <String>: --conversation-id 的别名
- --open-conversation-id <String>: --conversation-id 的别名
- --message-id <String>: 消息 openMsgId (必填)
- --emotion-id <String>: 表情 ID (必填)
- --emotion-name <String>: 表情名称 (必填)
- --text <String>: 文字内容 (必填)
- --background-id <String>: 背景 ID (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
