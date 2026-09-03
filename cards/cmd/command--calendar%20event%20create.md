# dws calendar event create

kind: command
completeness: partial
usage: dws calendar event create
description: Create a new calendar event on the user's calendar with title, time, attendees, and optional meeting room.
example: dws calendar event create --title "Q1 复盘会"
use_when: When the agent schedules a meeting or reminder on behalf of the user.
source: internal/helpers/calendar.go:232
visible_flags: 22
partial_reason: too_many_flags:22

## Flags
- --title <String>: 日程标题 (必填，最大2048字符)
- --start <String>: 开始时间 ISO-8601 (必填，例如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (必填，例如 2026-03-10T15:00:00+08:00)
- --timezone <String>: 时区 IANA 格式 (例如 Asia/Shanghai，默认 Asia/Shanghai)
- --desc <String>: 日程描述 (最大5000字符)
- --attendees <String>: 参会人 userId 列表，逗号分隔 (最多500人)，日程组织人自动放入参会人列表，无需传入userId
- --open-dingtalk-ids <String>: openDingTalkId 列表，逗号分隔 (与 --attendees 至少传一个)
- --rooms <String>: 会议室 roomId 列表，逗号分隔 (创建时直接预定，roomId 必须来自“room search”返回，若是循环会议，必须设置recurrence-end-date，避免长期预订)
- … 14 more; use dwsdoc cmd/short for full flags

## Related
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
- dws calendar event share-info
