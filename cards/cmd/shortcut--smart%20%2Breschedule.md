# dws smart +reschedule

kind: shortcut
completeness: full
usage: dws smart +reschedule
description: 改一个已有日程的时间（只动开始/结束时间，其他字段不变）
source: internal/shortcut/smart/reschedule.go:39
visible_flags: 3

## Flags
- --event <String>: 要改期的日程 eventId（可用 dws calendar event list 查询）
- --start <String>: 新的开始时间（ISO8601，如 2026-03-10T15:00:00+08:00）
- --end <String>: 新的结束时间（ISO8601，如 2026-03-10T16:00:00+08:00）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
