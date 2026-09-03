# dws calendar +room-find

kind: shortcut
completeness: full
description: 按时间段搜索可用会议室（不传时间默认当前起 1 小时）
source: internal/shortcut/calendar/calendar.go:433
visible_flags: 7

## Flags
- --start <String>: 开始时间 ISO-8601；起止时间必须是 RFC3339/ISO-8601，且 end 晚于 start
- --end <String>: 结束时间 ISO-8601；起止时间必须是 RFC3339/ISO-8601，且 end 晚于 start
- --available <Bool>: 仅返回可用会议室；保留已发布参数兼容性
- --group-id <String>: 会议室分组 ID
- --room-name <String>: 会议室名称过滤
- --limit <String>: 每页条数 (pageSize)；保留 string 类型兼容性；limit 必须在 1-100 之间
- --page <String>: 页码 (pageIndex，从 0 开始)；保留 string 类型兼容性；page 不能小于 0

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +freebusy
- dws calendar +room-groups
