# dws sheet new

kind: command
completeness: full
description: 新建工作表
source: internal/helpers/sheet_workbook.go:190
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID (必填)
- --name <String>: 工作表名称 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
