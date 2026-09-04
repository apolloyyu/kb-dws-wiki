# dws chat message list-topic-replies

kind: command
completeness: partial
usage: dws chat message list-topic-replies
description: —
example: dws chat message list-topic-replies --conversation-id <openconversation_id> --topic-id <topicId>
source: internal/helpers/chat.go:4460
visible_flags: 5
partial_reason: missing_description

## Flags
- --conversation-id <String> required: 群会话 openconversationId (必填)
- --topic-id <String> required: 话题 ID，由 dws chat message list 返回 (必填)
- --time <String>: 开始时间，格式: yyyy-MM-dd HH:mm:ss（可选）
- --limit <Int>: 返回数量（默认 50）
- --direction <String>: 时间方向: newer=从给定时间往现在拉，older=从给定时间往以前拉（推荐，默认 older）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
