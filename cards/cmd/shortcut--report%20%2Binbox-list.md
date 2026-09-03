# dws report +inbox-list

kind: shortcut
completeness: full
usage: dws report +inbox-list
description: 列出我收到的日志
source: internal/shortcut/report/report.go:78
visible_flags: 5

## Flags
- --start <String>: 开始时间 ISO-8601；结束时间必须晚于开始时间，跨度不得超过 180 天
- --end <String>: 结束时间 ISO-8601；结束时间必须晚于开始时间，跨度不得超过 180 天
- --cursor <Int>: —
- --size <Int>: —
- --sender-user-ids <StringSlice>: 发送人 staffId 列表

## Related
- dws report +outbox-list
- dws report +report-latest
- dws report +template-search
