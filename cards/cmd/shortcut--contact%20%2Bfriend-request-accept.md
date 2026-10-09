# dws contact +friend-request-accept

kind: shortcut
completeness: full
usage: dws contact +friend-request-accept
description: 同意指定用户发来的好友申请
source: internal/shortcut/contact/friend.go:259
visible_flags: 2

## Flags
- --from <String>: 对方开放钉钉号ID（openDingTalkId）；--from 不能为空白
- --alias <String>: 同意后为该好友设置的备注名（可选）

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +friend-request-send
- dws contact +get-roster
