# dws chat message list-all

kind: command
completeness: full
description: Search all messages across the current user's conversations within a time range, surfacing any search-entitlement guidance.
use_when: When the agent needs to audit or summarize everything the user saw across chats in a window.
source: internal/helpers/chat.go:4305
visible_flags: 4

## Flags
- --start <String>: 起始时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认当前时间前 1 天）
- --end <String>: 结束时间，格式: yyyy-MM-dd HH:mm:ss（可选，默认当前时间）
- --limit <Int>: 每页返回数量（默认 50）
- --cursor <String>: 分页游标（首页传 \"0\"，后续从响应中获取）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
