# dws calendar book get

kind: command
completeness: full
description: 获取日程详情
source: internal/helpers/calendar.go:178
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (默认 primary 主日历)

## Related
- dws calendar book list
- dws calendar book search
