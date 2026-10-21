# dws chat +broadcast

kind: shortcut
completeness: full
usage: dws chat +broadcast
description: 按姓名逐一给多个人群发同一条单聊消息（自动解析 userId、逐个发送）
source: internal/shortcut/smart/broadcast.go:40
visible_flags: 2

## Flags
- --to <StringSlice>: 收件人姓名/花名，逗号分隔的多个人
- --content <String>: 消息内容（支持 Markdown），所有人收到同一条

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +category-add-conversation
- dws chat +category-create
- dws chat +category-delete
