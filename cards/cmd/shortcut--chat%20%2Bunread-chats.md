# dws chat +unread-chats

kind: shortcut
completeness: full
usage: dws chat +unread-chats
description: 列出我有未读消息的会话（投影会话名/未读数/会话ID）
source: internal/shortcut/smart/unread_chats.go:48
visible_flags: 2

## Flags
- --count <Int>: 返回未读会话条数；显式 --count 必须大于 0，不传则使用服务端默认值
- --exclude-muted <Bool>: 是否排除已设置免打扰的会话（可选，默认 false）

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
