# dws chat message forward

kind: command
completeness: full
usage: dws chat message forward
description: 转发单条消息（源/目标会话均支持单聊/群聊）
example: dws chat message forward --src-conversation-id <srcOpenConversationId> --message-id <srcOpenMessageId> --dest-conversation-id <destOpenConversationId>
source: internal/helpers/chat.go:7906
visible_flags: 4

## Flags
- --src-conversation-id <String> required: 源会话 openConversationId (必填，支持单聊/群聊)
- --message-id <String> required: 源消息 openMessageId (必填)
- --dest-conversation-id <String> required: 目标会话 openConversationId (必填，支持单聊/群聊)
- --uuid <String>: 幂等键（可选）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
