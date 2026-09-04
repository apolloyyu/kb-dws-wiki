# dws chat message list-emotion-replies

kind: command
completeness: full
usage: dws chat message list-emotion-replies
description: 批量拉取消息的表情回复和文字回复
example: dws chat message list-emotion-replies --msg-ids msgId1,msgId2,msgId3
source: internal/helpers/chat.go:11092
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
