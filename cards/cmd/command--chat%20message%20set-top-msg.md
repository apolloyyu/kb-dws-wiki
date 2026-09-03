# dws chat message set-top-msg

kind: command
completeness: full
description: 置顶消息
source: internal/helpers/chat.go:9956
visible_flags: 2

## Flags
- --open-conversation-id <String> required: 会话 openConversationId (必填，支持群聊/单聊)
- --message-id <String> required: 消息 openMessageId (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
