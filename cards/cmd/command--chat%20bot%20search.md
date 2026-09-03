# dws chat bot search

kind: command
completeness: full
description: Search robots (bots) created by the current user by keyword.
use_when: When the agent needs to resolve one of its own bots by name to a robot code before sending bot messages.
source: internal/helpers/chat.go:1487
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --limit <Int>: 每页返回数量（默认 20）
- --cursor <String>: 分页游标（默认 \"0\"，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已设置免打扰的群聊（默认 false）

## Related
- dws chat bot find
