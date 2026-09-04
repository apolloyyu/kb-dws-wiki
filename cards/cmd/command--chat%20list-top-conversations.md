# dws chat list-top-conversations

kind: command
completeness: full
usage: dws chat list-top-conversations
description: Fetch the list of conversations the current user has pinned to the top of their chat list.
example: dws chat list-top-conversations --limit 1000
use_when: When the agent needs to prioritize the user's most important conversations in a summary or dashboard.
source: internal/helpers/chat.go:4686
visible_flags: 3

## Flags
- --limit <Int>: 每页返回数量（默认 1000）
- --cursor <Int64>: 分页游标（首次不传或传 0，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已设置免打扰的会话（默认 false）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
