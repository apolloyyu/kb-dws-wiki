# dws aitable chart share get

kind: command
completeness: full
usage: dws aitable chart share get
description: Retrieve the current public-sharing configuration of a chart, including share link and permissions.
example: dws aitable chart share get --base-id BASE_ID --dashboard-id DASHBOARD_ID --chart-id CHART_ID
use_when: When the agent needs to check whether a chart is already shared externally before issuing a link.
source: internal/helpers/aitable.go:6792
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --chart-id <String>: 目标 Chart ID (必填)

## Related
- dws aitable chart share update
