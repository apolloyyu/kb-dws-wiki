# dws report entry stats

kind: command
completeness: full
usage: dws report entry stats
description: 读取单份日报的已读统计
example: dws report entry stats --report-id <reportId>
source: internal/helpers/report.go:236
visible_flags: 1

## Flags
- --report-id <String>: 日志 ID (必填)

## Related
- dws report entry get
- dws report entry submit
