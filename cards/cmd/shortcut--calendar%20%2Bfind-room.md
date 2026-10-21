# dws calendar +find-room

kind: shortcut
completeness: full
usage: dws calendar +find-room
description: 查询指定时间段内所有可用的会议室
source: internal/shortcut/smart/find_room.go:44
visible_flags: 2

## Flags
- --start <String>: 开始时间（ISO8601，如 2026-03-10T14:00:00+08:00，需为未来时间）
- --end <String>: 结束时间（ISO8601，如 2026-03-10T15:00:00+08:00）

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +cancel-event
