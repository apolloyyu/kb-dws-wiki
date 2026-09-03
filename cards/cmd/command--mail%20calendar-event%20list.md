# dws mail calendar-event list

kind: command
completeness: full
usage: dws mail calendar-event list
description: 查询指定日历时间范围内的日程
example: dws mail calendar-event list --email user@company.com --id <calendarFolderId> --start "2026-07-01T00:00:00Z" --end "2026-07-31T23:59:59Z"
source: internal/helpers/mail.go:3772
visible_flags: 5

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 日历文件夹ID (必填)
- --start <String>: 视图开始UTC时间 (必填)
- --end <String>: 视图结束UTC时间 (必填)
- --cursor <String>: 分页光标 (可选)

## Related
- none
