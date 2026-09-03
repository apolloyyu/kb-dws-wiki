# dws calendar event share-info

kind: command
completeness: full
usage: dws calendar event share-info
description: 获取日程的分享信息
example: dws calendar event share-info --id EVENT_ID
source: internal/helpers/calendar.go:2087
visible_flags: 3

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (默认 primary 主日历)
- --language <String>: 语言代码 (可选，如 zh-CN)

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
