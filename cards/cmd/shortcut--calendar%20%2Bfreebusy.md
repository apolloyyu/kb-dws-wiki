# dws calendar +freebusy

kind: shortcut
completeness: full
usage: dws calendar +freebusy
description: 查询用户 / 会议室闲忙状态（--users 与 --rooms 至少其一）
source: internal/shortcut/calendar/calendar.go:678
visible_flags: 4

## Flags
- --users <StringSlice>: 用户 userId 列表 (逗号分隔)
- --rooms <StringSlice>: 会议室 roomId 列表 (逗号分隔)
- --start <String>: 开始时间 ISO-8601
- --end <String>: 结束时间 ISO-8601

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +room-find
- dws calendar +room-groups
