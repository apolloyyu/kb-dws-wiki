# dws contact +friend-request-reject

kind: shortcut
completeness: full
usage: dws contact +friend-request-reject
description: 删除（忽略）指定用户发来的好友申请
source: internal/shortcut/contact/friend.go:313
visible_flags: 1

## Flags
- --from <String>: 对方开放钉钉号ID（openDingTalkId）；--from 不能为空白

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-send
- dws contact +get-roster
