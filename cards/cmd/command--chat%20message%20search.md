# dws chat message search

kind: command
completeness: full
description: Search messages by keyword across the user's conversations.
use_when: When the agent needs to locate a specific statement or link the user remembers from chat history.
source: internal/helpers/chat.go:1487
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已设置免打扰的群聊（默认 false）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
