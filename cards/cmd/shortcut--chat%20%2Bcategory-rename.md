# dws chat +category-rename

kind: shortcut
completeness: full
usage: dws chat +category-rename
description: 更新用户自定义会话分组的名称
source: internal/shortcut/chat/chat_conversation.go:1142
visible_flags: 2

## Flags
- --category-id <Int>: 会话分组 ID
- --title <String>: 新的分组名称；去除首尾空白后必须非空，且最多 15 个字符

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
- dws chat +category-list
