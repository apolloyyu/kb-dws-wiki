# dws contact +friend-request-list

kind: shortcut
completeness: full
usage: dws contact +friend-request-list
description: 查询当前用户收到的好友申请列表
source: internal/shortcut/contact/friend.go:120
visible_flags: 2

## Flags
- --cursor <Int>: 分页游标；首页不传，翻页时传上一页返回的 cursor（--cursor 必须大于或等于 0）
- --size <Int>: 每页数量（--size 必须大于 0 且不超过 100），默认 20

## Related
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-reject
- dws contact +friend-request-send
- dws contact +get-roster
