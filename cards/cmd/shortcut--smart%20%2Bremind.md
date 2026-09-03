# dws smart +remind

kind: shortcut
completeness: full
description: 给自己创建一条带可选截止时间的待办
source: internal/shortcut/smart/remind.go:44
visible_flags: 2

## Flags
- --task <String>: 待办标题/内容
- --at <String>: 截止时间（ISO8601，可选，写入 dueTime，不是提醒时间）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
