# dws chat list-all-conversations

kind: command
completeness: full
usage: dws chat list-all-conversations
description: 分页获取当前用户的全部会话列表
example: dws chat list-all-conversations
source: internal/helpers/chat.go:9955
visible_flags: 3

## Flags
- --limit <Int>: 每页数量（1-100，默认 100）
- --cursor <Int64>: 分页游标（首次不传或传 0，翻页传 nextCursor）
- --exclude-muted <Bool>: 是否排除已免打扰会话（默认 false）

## Related
- dws chat bot
- dws chat category
- dws chat chmod
- dws chat clear-all-red-point
- dws chat clear-messages
- dws chat clear-red-point
