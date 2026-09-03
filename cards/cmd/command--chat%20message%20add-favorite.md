# dws chat message add-favorite

kind: command
completeness: full
usage: dws chat message add-favorite
description: 收藏指定消息
example: dws chat message add-favorite --open-message-id <openMessageId> --open-conversation-id <openConversationId>
source: internal/helpers/chat.go:9170
visible_flags: 2

## Flags
- --open-message-id <String> required: 消息 openMessageId (必填)
- --open-conversation-id <String> required: 消息所在会话的 openConversationId (必填，支持群聊/单聊)

## Related
- dws chat message add-emoji
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
- dws chat message edit
