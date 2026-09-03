# dws sheet chart list

kind: command
completeness: full
description: 获取浮动图表
source: internal/helpers/sheet_chart.go:126
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --chart-id <String>: 浮动图表 ID (可选，不传则返回全部)

## Related
- dws sheet chart create
- dws sheet chart delete
- dws sheet chart update
