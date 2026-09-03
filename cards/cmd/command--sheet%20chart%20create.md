# dws sheet chart create

kind: command
completeness: full
usage: dws sheet chart create
description: 创建浮动图表
example: dws sheet chart create --node NODE_ID --sheet-id SHEET_ID --properties '{
source: internal/helpers/sheet_chart.go:184
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID (必填)
- --properties <String>: 图表完整配置 JSON (必填，含 position/dimensions/chart)

## Related
- dws sheet chart delete
- dws sheet chart list
- dws sheet chart update
