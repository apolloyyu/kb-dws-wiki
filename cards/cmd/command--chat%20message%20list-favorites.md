# dws chat message list-favorites

kind: command
completeness: partial
usage: dws chat message list-favorites
description: 查询收藏的消息列表
example: dws chat message list-favorites
source: internal/helpers/chat.go:9470
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --cursor <Int64>: 数字分页游标（默认 0；翻页时传上次返回的 nextCursor）
- --size <Int>: 一次拉取的收藏数量（默认 20，范围 1-30）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
