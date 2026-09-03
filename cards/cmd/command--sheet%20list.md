# dws sheet list

kind: command
completeness: full
usage: dws sheet list
description: 获取全部工作表列表
example: dws sheet list --node NODE_ID
source: internal/helpers/sheet_workbook.go:73
visible_flags: 1

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
