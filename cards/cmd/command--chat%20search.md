# dws chat search

kind: command
completeness: full
description: Search group conversations the user belongs to by group name keyword.
use_when: When the agent needs to resolve a group name to a conversation ID.
source: internal/helpers/chat.go:1487
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已设置免打扰的群聊（默认 false）

## Related
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
- dws chat conversation-info
- dws chat emotion
