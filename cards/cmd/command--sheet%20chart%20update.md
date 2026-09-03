# dws sheet chart update

kind: command
completeness: full
usage: dws sheet chart update
description: 更新浮动图表
example: dws sheet chart update --node NODE_ID --sheet-id SHEET_ID --chart-id CHART_ID --properties '{
source: internal/helpers/sheet_chart.go:286
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID (必填)
- --chart-id <String>: 浮动图表 ID (必填，可通过 chart list 获取)
- --properties <String>: 图表完整配置 JSON (必填，PUT 语义整体覆盖)

## Related
- dws sheet chart create
- dws sheet chart delete
- dws sheet chart list
