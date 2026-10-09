# dws contact +friend-request-send

kind: shortcut
completeness: full
usage: dws contact +friend-request-send
description: 向指定用户发起好友申请
source: internal/shortcut/contact/friend.go:205
visible_flags: 2

## Flags
- --to <String>: 对方开放钉钉号ID（openDingTalkId）；--to 不能为空白
- --remark <String>: 好友申请验证留言（可选）

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
- dws contact +get-roster
