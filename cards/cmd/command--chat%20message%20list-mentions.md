# dws chat message list-mentions

kind: command
completeness: full
description: Fetch messages where the current user was @-mentioned.
use_when: When the agent wants to surface items that explicitly require the user's attention.
source: internal/helpers/chat.go:4404
visible_flags: 5

## Flags
- --conversation-id <String>: 群聊 openconversation_id（可选，不传则查全部）
- --start <String>: 开始时间，ISO-8601 格式（可选，默认当前时间前 7 天）
- --end <String>: 结束时间，ISO-8601 格式（可选，默认当前时间）
- --limit <Int>: 每页返回数量（默认 50）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
