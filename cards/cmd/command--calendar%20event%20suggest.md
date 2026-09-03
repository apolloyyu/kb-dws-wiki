# dws calendar event suggest

kind: command
completeness: full
description: Suggest candidate meeting time slots based on participants' busy/free data and constraints.
use_when: When the agent is coordinating a meeting and wants ranked time suggestions rather than raw busy data.
source: internal/helpers/calendar.go:503
visible_flags: 5

## Flags
- --start <String>: 推荐时间范围开始 ISO-8601 (默认当前时间)
- --end <String>: 推荐时间范围结束 ISO-8601 (默认次日18点)
- --timezone <String>: 时区 IANA 格式 (默认 Asia/Shanghai)
- --users <String>: 参会人 userId 列表，逗号分隔
- --duration <String>: 日程持续时间 (分钟，默认30)

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
