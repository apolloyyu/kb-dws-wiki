# dws report stats

kind: command
completeness: full
description: Retrieve aggregated statistics for a report entry by ID (views, likes, comments, etc.).
use_when: When the agent measures engagement or reach of a report the user sent.
source: internal/helpers/report.go:236
visible_flags: 0

## Flags
- none

## Related
- dws report create
- dws report detail
- dws report list
- dws report sent
