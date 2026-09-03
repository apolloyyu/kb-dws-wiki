# dws chat search-common

kind: command
completeness: full
usage: dws chat search-common
description: Find group chats the current user and a specified other user both belong to.
example: dws chat search-common --nicks "风雷,山乔" --limit 20 --cursor 0
use_when: When the agent needs an existing shared channel to contact another user without creating a new group.
source: internal/helpers/chat.go:5001
visible_flags: 5

## Flags
- --nicks <String> required: 要搜索的昵称列表，逗号分隔 (必填)
- --match-mode <String>: 匹配模式：AND=所有人都在群里，OR=任一人在群里（默认 AND）
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
