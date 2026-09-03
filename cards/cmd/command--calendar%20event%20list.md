# dws calendar event list

kind: command
completeness: full
description: List calendar events on the user's calendar within a given time range.
use_when: When the agent needs an overview of the user's upcoming schedule or a day's agenda.
source: internal/helpers/calendar.go:72
visible_flags: 5

## Flags
- --start <String>: 开始时间 ISO-8601 (例如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (例如 2026-03-10T18:00:00+08:00)
- --calendar-id <String>: 日历 ID (默认 primary 主日历，仅在查询其他日历本时填写)
- --cursor <String>: 分页游标 (首次查询无需传入，仅翻页时传入上一次返回的 nextCursor)
- --limit <Int>: 每页返回条数 (默认 100，最大 100)

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event respond
- dws calendar event share-info
