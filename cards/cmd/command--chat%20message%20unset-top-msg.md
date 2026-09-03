# dws chat message unset-top-msg

kind: command
completeness: full
usage: dws chat message unset-top-msg
description: 取消置顶消息
example: dws chat message unset-top-msg --open-conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat.go:10016
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
