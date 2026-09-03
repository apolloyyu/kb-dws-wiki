# dws sheet show-gridline

kind: command
completeness: full
usage: dws sheet show-gridline
description: 显示工作表网格线
example: dws sheet show-gridline --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_workbook.go:500
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
