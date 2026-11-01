# dws aitable dashboard arrange

kind: command
completeness: full
usage: dws aitable dashboard arrange
description: 统一按行重排仪表盘图表位置和尺寸
example: dws aitable dashboard arrange --base-id BASE_ID --dashboard-id DASHBOARD_ID
source: internal/helpers/aitable.go:8042
visible_flags: 4

## Flags
- --expected-layout-fingerprint <String>: 本次真实预览的 source 摘要；变化时停止，非原子 CAS
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
