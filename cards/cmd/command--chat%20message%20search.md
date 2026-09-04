# dws chat message search

kind: command
completeness: partial
usage: dws chat message search
description: Search messages by keyword across the user's conversations.
example: dws chat message search --query "changefree" --start "2026-04-01T00:00:00+08:00" --end "2026-04-15T00:00:00+08:00" --limit 50 --cursor 0
use_when: When the agent needs to locate a specific statement or link the user remembers from chat history.
source: internal/helpers/chat.go:4779
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --query <String>: 搜索关键词 (必填)
- --conversation-id <String>: 群聊 openconversation_id（可选，不传则搜索所有会话）
- --start <String>: 开始时间，ISO-8601 格式（可选，默认当前时间前 7 天）
- --end <String>: 结束时间，ISO-8601 格式（可选，默认当前时间）
- --limit <Int>: 每页返回数量（默认 100）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
