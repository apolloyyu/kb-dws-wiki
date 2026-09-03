# dws smart +my-free

kind: shortcut
completeness: full
description: 查我自己在某时间段的忙闲（默认今天，无需输入姓名）
source: internal/shortcut/smart/my_free.go:42
visible_flags: 2

## Flags
- --start <String>: 开始时间（ISO8601，可选，默认今天 00:00）
- --end <String>: 结束时间（ISO8601，可选，默认次日 00:00）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
