# dws chat +category-create

kind: shortcut
completeness: full
usage: dws chat +category-create
description: 创建用户自定义会话分组
source: internal/shortcut/chat/chat_conversation.go:1048
visible_flags: 1

## Flags
- --title <String>: 分组名称；去除首尾空白后必须非空，且最多 15 个字符

## Related
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-delete
- dws chat +category-list
- dws chat +category-list-conversations
