# dws sheet hide-gridline

kind: command
completeness: full
usage: dws sheet hide-gridline
description: 隐藏工作表网格线
example: dws sheet hide-gridline --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_workbook.go:553
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
