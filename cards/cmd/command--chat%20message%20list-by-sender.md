# dws chat message list-by-sender

kind: command
completeness: full
description: Fetch messages authored by a specific sender across both single and group chats.
use_when: When the agent needs to pull everything a particular colleague said recently.
source: internal/helpers/chat.go:4352
visible_flags: 6

## Flags
- --sender-user-id <String>: 发送者 userId（与 --sender-open-dingtalk-id 二选一）
- --sender-open-dingtalk-id <String>: 发送者 openDingTalkId（与 --sender-user-id 二选一，适用于无法获取 userId 的场景）
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
