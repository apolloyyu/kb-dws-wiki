# dws report entry get

kind: command
completeness: full
usage: dws report entry get
description: 读取单份日报正文（含字段明细 + 钉钉跳转链接）
example: dws report entry get --report-id <reportId>
source: internal/helpers/report.go:190
visible_flags: 1

## Flags
- --report-id <String>: 日志 ID (必填)

## Related
- dws report entry stats
- dws report entry submit
