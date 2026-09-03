# dws sheet chart delete

kind: command
completeness: full
usage: dws sheet chart delete
description: 删除浮动图表
example: dws sheet chart delete --node NODE_ID --sheet-id SHEET_ID --chart-id CHART_ID --yes
source: internal/helpers/sheet_chart.go:371
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --chart-id <String>: 浮动图表 ID (必填，可通过 chart list 获取)

## Related
- dws sheet chart create
- dws sheet chart list
- dws sheet chart update
