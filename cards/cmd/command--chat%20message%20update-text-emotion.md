# dws chat message update-text-emotion

kind: command
completeness: full
description: 更新消息的文字表情回应
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
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
