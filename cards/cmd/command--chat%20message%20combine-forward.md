# dws chat message combine-forward

kind: command
completeness: full
usage: dws chat message combine-forward
description: 合并转发多条消息
example: dws chat message combine-forward --src-conversation-id <srcOpenCid> --msg-ids <id1>,<id2>,<id3> --dest-conversation-id <destOpenCid>
source: internal/helpers/chat.go:8887
visible_flags: 4

## Flags
- --src-conversation-id <String> required: 源会话 openConversationId (必填，支持单聊/群聊)
- --msg-ids <String> required: 源消息 openMessageId 列表，逗号分隔 (必填)
- --dest-conversation-id <String> required: 目标会话 openConversationId (必填，支持单聊/群聊)
- --uuid <String>: 幂等键（可选）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message create-text-emotion
- dws chat message download-media
- dws chat message edit
