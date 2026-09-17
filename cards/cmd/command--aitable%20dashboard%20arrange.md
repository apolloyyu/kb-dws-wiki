# dws aitable dashboard arrange

kind: command
completeness: full
usage: dws aitable dashboard arrange
description: 自动重排仪表盘图表布局
example: dws aitable dashboard arrange --base-id BASE_ID --dashboard-id DASHBOARD_ID
source: internal/helpers/aitable.go:7888
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)
- --is-app-mode <Bool>: 可选，只读的应用模式上下文；仅在确认目标属于应用模式时传 true，强制按 V2 48 列对齐；不传时按已验证的 schemaVersion 选择列数

## Related
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard get
- dws aitable dashboard share
- dws aitable dashboard update
