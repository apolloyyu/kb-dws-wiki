# dws chat message list-focused

kind: command
completeness: partial
usage: dws chat message list-focused
description: Fetch messages from users the current user has marked as "special focus" (starred contacts).
example: dws chat message list-focused --limit 50
use_when: When the agent builds a priority-inbox view highlighting messages from important people.
source: internal/helpers/chat.go:4642
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --limit <Int>: 每页返回数量（默认 50）
- --cursor <Int64>: 分页游标（首次不传或传 0，翻页传 nextCursor）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
