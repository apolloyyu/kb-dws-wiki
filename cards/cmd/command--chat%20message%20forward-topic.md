# dws chat message forward-topic

kind: command
completeness: partial
usage: dws chat message forward-topic
description: —
example: dws chat message forward-topic --src-msg-id <srcOpenMessageId> --src-conversation-id <srcOpenConversationId> --src-thread-id <srcOpenConvThreadId> --dest-conversation-id <destOpenConversationId>
source: internal/helpers/chat.go:9157
visible_flags: 4
partial_reason: missing_description

## Flags
- --src-msg-id <String> required: 源消息 openMessageId (必填，要转发的消息)
- --src-conversation-id <String> required: 源会话 openConversationId (必填，消息所在的会话)
- --src-thread-id <String> required: 话题 ID (必填，格式: convThread + 加密后的convThreadId)
- --dest-conversation-id <String> required: 目标会话 openConversationId (必填，转发到的会话)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
