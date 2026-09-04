# dws chat search

kind: command
completeness: full
usage: dws chat search [query]
description: Search group conversations the user belongs to by group name keyword.
example: dws chat search --query "项目冲刺"
use_when: When the agent needs to resolve a group name to a conversation ID.
source: internal/helpers/chat.go:1670
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已设置免打扰的群聊（默认 false）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
