# dws calendar event create

kind: command
completeness: partial
usage: dws calendar event create
description: Create a new calendar event on the user's calendar with title, time, attendees, and optional meeting room.
example: dws calendar event create --title "Q1 复盘会"
use_when: When the agent schedules a meeting or reminder on behalf of the user.
source: internal/helpers/calendar.go:232
visible_flags: 24
partial_reason: too_many_flags:24

## Flags
- --title <String>: 日程标题 (必填，最大2048字符)
- --start <String>: 开始时间 (必填；全天为 yyyy-MM-dd，否则为 ISO-8601，如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 (必填；全天为 yyyy-MM-dd 且不包含当天，否则为 ISO-8601，如 2026-03-10T15:00:00+08:00)
- --is-all-day <Bool>: 全天日程；true 时起止时间使用 yyyy-MM-dd，不传则不发送此字段
- --add-online-meeting <Bool>: 添加视频会议（不传沿用服务端默认添加；无需添加时传 false）
- --timezone <String>: 时区 IANA 格式 (例如 Asia/Shanghai，默认 Asia/Shanghai)
- --desc <String>: 日程描述 (最大5000字符)
- --attendees <String>: 参会人 userId 列表，逗号分隔 (最多500人)，日程组织人自动放入参会人列表，无需传入userId
- … 16 more; use dwsdoc cmd/short for full flags

## Related
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
- dws calendar event share-info
