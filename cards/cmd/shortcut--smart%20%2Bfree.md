# dws smart +free

kind: shortcut
completeness: full
usage: dws smart +free
description: 按姓名查询某人在指定时间段内的忙闲状态（自动解析 userId）
source: internal/shortcut/smart/freebusy.go:36
visible_flags: 3

## Flags
- --who <String>: 要查忙闲的人的姓名/花名
- --start <String>: 开始时间（ISO8601，如 2026-03-10T14:00:00+08:00）
- --end <String>: 结束时间（ISO8601，如 2026-03-10T18:00:00+08:00）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
