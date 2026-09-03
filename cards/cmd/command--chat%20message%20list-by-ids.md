# dws chat message list-by-ids

kind: command
completeness: full
description: 根据消息 ID 批量查询消息
source: internal/helpers/chat.go:6197
visible_flags: 1

## Flags
- --msg-ids <String> required: 消息 ID 列表，逗号分隔，最多 50 条 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
