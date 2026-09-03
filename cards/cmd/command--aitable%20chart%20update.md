# dws aitable chart update

kind: command
completeness: full
usage: dws aitable chart update
description: Update an existing chart's configuration (type, dimensions, metrics, style).
example: dws aitable chart update --base-id BASE_ID --dashboard-id DASHBOARD_ID --chart-id CHART_ID
use_when: When the agent iterates on a chart's visualization after reviewing the initial result.
source: internal/helpers/aitable.go:6680
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --chart-id <String>: 目标 Chart ID (必填)
- --config <String>: 图表配置 JSON (必填)
- --layout <String>: 图表布局更新 JSON

## Related
- dws aitable chart create
- dws aitable chart delete
- dws aitable chart get
- dws aitable chart share
- dws aitable chart widgets-example
