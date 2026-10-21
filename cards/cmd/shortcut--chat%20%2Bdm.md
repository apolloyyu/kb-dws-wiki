# dws chat +dm

kind: shortcut
completeness: full
usage: dws chat +dm
description: 按姓名直接给某人发单聊消息（自动解析唯一 openDingTalkId）
source: internal/shortcut/smart/dm.go:37
visible_flags: 2

## Flags
- --to <String>: 收件人姓名/花名
- --content <String>: 消息内容（支持 Markdown）

## Related
- dws chat +at-me
- dws chat +bot-find
- dws chat +bot-search
- dws chat +broadcast
- dws chat +category-add-conversation
- dws chat +category-create
