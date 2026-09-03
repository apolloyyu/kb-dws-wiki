# dws calendar event instances

kind: command
completeness: full
description: 查询循环日程的实例列表
source: internal/helpers/calendar.go:1911
visible_flags: 6

## Flags
- --id <String>: 日程 ID (必填)
- --start <String>: 开始时间 ISO-8601 (例如 2026-03-10T00:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (例如 2026-03-31T23:59:59+08:00)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)
- --cursor <String>: 分页游标 (首次查询无需传入，仅翻页时传入上一次返回的 nextCursor)
- --limit <Int>: 每页返回条数 (默认 100，最大 100)

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event list
- dws calendar event respond
- dws calendar event share-info
