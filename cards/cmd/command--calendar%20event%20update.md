# dws calendar event update

kind: command
completeness: partial
usage: dws calendar event update
description: Update an existing calendar event's fields such as time, title, participants, or location.
example: dws calendar event update --id EVENT_ID --title "新标题"
use_when: When the agent needs to reschedule or amend a previously created event.
source: internal/helpers/calendar.go:373
visible_flags: 21
partial_reason: too_many_flags:21

## Flags
- --id <String>: 日程 ID (必填)
- --title <String>: 新标题
- --start <String>: 新开始时间 (全天为 yyyy-MM-dd，否则为 ISO-8601)
- --end <String>: 新结束时间 (全天为 yyyy-MM-dd 且不包含当天，否则为 ISO-8601)
- --desc <String>: 新描述 (最大5000字符)
- --is-all-day <Bool>: 全天状态；显式设置时必须重传 --start/--end，true 使用 yyyy-MM-dd，false 使用带时区 ISO-8601
- --add-online-meeting <Bool>: 添加视频会议（不传沿用原有更新逻辑；true 重新添加并覆盖已有会议，false 保留已有会议）
- --timezone <String>: 时区 IANA 格式 (例如 Asia/Shanghai)
- … 13 more; use dwsdoc cmd/short for full flags

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
