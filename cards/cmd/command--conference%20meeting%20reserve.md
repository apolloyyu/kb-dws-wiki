# dws conference meeting reserve

kind: command
completeness: full
usage: dws conference meeting reserve
description: 预约会议（已下线）
example: dws conference meeting reserve --title "产品评审会"
source: internal/helpers/conference.go:46
visible_flags: 3

## Flags
- --title <String>: 会议标题 (必填)
- --start <String>: 开始时间 ISO-8601 格式，如 2026-03-11T14:00:00+08:00 (必填)
- --end <String>: 结束时间 ISO-8601 格式，如 2026-03-11T15:00:00+08:00 (必填)

## Related
- none
