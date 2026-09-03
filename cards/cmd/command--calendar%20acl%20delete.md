# dws calendar acl delete

kind: command
completeness: full
description: 删除日程
source: internal/helpers/calendar.go:453
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)

## Related
- dws calendar acl list
