# dws calendar +room-search

kind: shortcut
completeness: full
description: 按名称模糊搜索会议室（不检查可用性）
source: internal/shortcut/calendar/calendar.go:331
visible_flags: 1

## Flags
- --room-name <String>: 会议室名称（精简核心专名，剔除“会议室”等后缀）

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +freebusy
- dws calendar +room-find
