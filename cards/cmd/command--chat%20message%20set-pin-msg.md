# dws chat message set-pin-msg

kind: command
completeness: full
usage: dws chat message set-pin-msg
description: 钉住消息（Pin）
example: dws chat message set-pin-msg --open-conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat.go:9194
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
