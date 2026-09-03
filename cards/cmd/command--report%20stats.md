# dws report stats

kind: command
completeness: full
usage: dws report stats
description: Retrieve aggregated statistics for a report entry by ID (views, likes, comments, etc.).
example: dws report stats --report-id <reportId>
use_when: When the agent measures engagement or reach of a report the user sent.
source: internal/helpers/report.go:491
visible_flags: 1

## Flags
- --report-id <String>: 日志 ID (必填)

## Related
- dws report create
- dws report created
- dws report detail
- dws report entry
- dws report inbox
- dws report list
