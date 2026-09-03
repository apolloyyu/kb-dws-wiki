# dws chat message list-emotion-replies

kind: command
completeness: full
description: 批量拉取消息的表情回复和文字回复
source: internal/helpers/chat.go:10890
visible_flags: 1

## Flags
- --msg-ids <String> required: 消息 ID 列表，逗号分隔 (必填)

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
