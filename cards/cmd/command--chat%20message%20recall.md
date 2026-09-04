# dws chat message recall

kind: command
completeness: full
usage: dws chat message recall
description: 撤回用户发送的消息
example: dws chat message recall --conversation-id <openConversationId> --message-id <openMessageId>
source: internal/helpers/chat.go:4977
visible_flags: 2

## Flags
- --conversation-id <String>: 会话 openConversationId (必填)
- --message-id <String> required: 消息 openMessageId (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
