# dws aitable chart get

kind: command
completeness: full
usage: dws aitable chart get
description: Retrieve a chart's full configuration and metadata.
example: dws aitable chart get --base-id BASE_ID --dashboard-id DASHBOARD_ID --chart-id CHART_ID
use_when: When the agent needs to inspect an existing chart to clone it or adjust its configuration.
source: internal/helpers/aitable.go:6584
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --chart-id <String>: 目标 Chart ID（通过 dashboard get 获取）(必填)

## Related
- dws aitable chart create
- dws aitable chart delete
- dws aitable chart share
- dws aitable chart update
- dws aitable chart widgets-example
