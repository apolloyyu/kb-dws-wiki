# dws smart +dm

kind: shortcut
completeness: full
usage: dws smart +dm
description: 按姓名直接给某人发单聊消息（自动解析唯一 openDingTalkId）
source: internal/shortcut/smart/dm.go:37
visible_flags: 2

## Flags
- --to <String>: 收件人姓名/花名
- --content <String>: 消息内容（支持 Markdown）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
