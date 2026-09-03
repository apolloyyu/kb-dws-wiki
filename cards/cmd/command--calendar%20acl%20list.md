# dws calendar acl list

kind: command
completeness: full
description: 查询日程列表
source: internal/helpers/calendar.go:72
visible_flags: 5

## Flags
- --start <String>: 开始时间 ISO-8601 (例如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (例如 2026-03-10T18:00:00+08:00)
- --calendar-id <String>: 日历 ID (默认 primary 主日历，仅在查询其他日历本时填写)
- --cursor <String>: 分页游标 (首次查询无需传入，仅翻页时传入上一次返回的 nextCursor)
- --limit <Int>: 每页返回条数 (默认 100，最大 100)

## Related
- dws calendar acl delete
