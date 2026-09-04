# dws aitable chart delete

kind: command
completeness: full
usage: dws aitable chart delete
description: Delete a chart from a Base by chart ID.
example: dws aitable chart delete --base-id BASE_ID --dashboard-id DASHBOARD_ID --chart-id CHART_ID --yes
use_when: When the agent needs to remove an obsolete or mistakenly-created chart.
source: internal/helpers/aitable.go:6753
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --chart-id <String>: 目标 Chart ID (必填)
- --reason <String>: 删除原因

## Related
- dws aitable chart create
- dws aitable chart get
- dws aitable chart share
- dws aitable chart update
- dws aitable chart widgets-example
