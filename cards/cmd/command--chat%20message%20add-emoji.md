# dws chat message add-emoji

kind: command
completeness: full
usage: dws chat message add-emoji
description: 对消息添加 emoji 表情回应
example: dws chat message add-emoji --conversation-id <openConversationId> --message-id <openMsgId> --emoji "赞"
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
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
- dws chat message edit
