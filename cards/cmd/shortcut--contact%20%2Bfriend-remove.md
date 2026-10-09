# dws contact +friend-remove

kind: shortcut
completeness: full
usage: dws contact +friend-remove
description: 删除指定好友
source: internal/shortcut/contact/friend.go:363
visible_flags: 1

## Flags
- --friend <String>: 要删除的好友开放钉钉号ID（openDingTalkId）；--friend 不能为空白

## Related
- dws contact +friend-list
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +friend-request-send
- dws contact +get-roster
