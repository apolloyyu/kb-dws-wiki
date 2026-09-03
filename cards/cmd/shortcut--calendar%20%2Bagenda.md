# dws calendar +agenda

kind: shortcut
completeness: full
description: 查询日程列表（不传时间默认查询今天）
source: internal/shortcut/calendar/calendar.go:48
visible_flags: 5

## Flags
- --start <String>: 开始时间 ISO-8601；起止时间必须是 RFC3339/ISO-8601，且 end 晚于 start；默认今天 00:00
- --end <String>: 结束时间 ISO-8601；起止时间必须是 RFC3339/ISO-8601，且 end 晚于 start；默认今天 23:59
- --calendar-id <String>: 日历 ID (默认 primary 主日历)
- --cursor <String>: 分页游标 (上一次返回的 nextCursor)
- --limit <Int>: 每页返回条数（服务端默认 100）；limit 必须在 1-100 之间

## Related
- dws calendar +attendee-list
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +freebusy
- dws calendar +room-find
- dws calendar +room-groups
