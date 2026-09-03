# dws sheet delete-sheet

kind: command
completeness: full
usage: dws sheet delete-sheet
description: 删除工作表
example: dws sheet delete-sheet --node NODE_ID --sheet-id SHEET_ID --yes
source: internal/helpers/sheet_workbook.go:449
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 要删除的工作表 ID 或名称 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
