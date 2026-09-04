# dws aitable dashboard arrange

kind: command
completeness: full
usage: dws aitable dashboard arrange
description: 自动重排仪表盘图表布局
example: dws aitable dashboard arrange --base-id BASE_ID --dashboard-id DASHBOARD_ID
source: internal/helpers/aitable.go:6414
visible_flags: 2

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)

## Related
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard get
- dws aitable dashboard share
- dws aitable dashboard update
