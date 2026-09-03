# dws calendar event update

kind: command
completeness: partial
usage: dws calendar event update
description: Update an existing calendar event's fields such as time, title, participants, or location.
example: dws calendar event update --id EVENT_ID --title "新标题"
use_when: When the agent needs to reschedule or amend a previously created event.
source: internal/helpers/calendar.go:356
visible_flags: 19
partial_reason: too_many_flags:19

## Flags
- --id <String>: 日程 ID (必填)
- --title <String>: 新标题
- --start <String>: 新开始时间 ISO-8601
- --end <String>: 新结束时间 ISO-8601
- --desc <String>: 新描述 (最大5000字符)
- --timezone <String>: 时区 IANA 格式 (例如 Asia/Shanghai)
- --recurrence-type <String>: [recurrence整体必填] 循环类型: daily|weekly|absoluteMonthly|relativeMonthly|absoluteYearly；MCP 不合并部分字段，修改任一循环字段都要重传完整 pattern+range
- --recurrence-interval <Int>: [recurrence整体必填] 循环间隔 (>0；如 daily 时表示每N天，weekly 时表示每N周)
- … 11 more; use dwsdoc cmd/short for full flags

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
