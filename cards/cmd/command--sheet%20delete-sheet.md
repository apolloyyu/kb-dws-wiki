# dws sheet delete-sheet

kind: command
completeness: full
description: 删除工作表
source: internal/helpers/sheet_workbook.go:449
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 要删除的工作表 ID 或名称 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
