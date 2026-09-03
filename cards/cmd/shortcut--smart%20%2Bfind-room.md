# dws smart +find-room

kind: shortcut
completeness: full
description: 查询指定时间段内所有可用的会议室
source: internal/shortcut/smart/find_room.go:44
visible_flags: 2

## Flags
- --start <String>: 开始时间（ISO8601，如 2026-03-10T14:00:00+08:00，需为未来时间）
- --end <String>: 结束时间（ISO8601，如 2026-03-10T15:00:00+08:00）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
