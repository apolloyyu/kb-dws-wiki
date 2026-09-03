# dws sheet table-get

kind: command
completeness: full
usage: dws sheet table-get
description: 读取结构化 table 数据
example: dws sheet table-get --node NODE_ID
source: internal/helpers/sheet_table.go:29
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称
- --range <String>: 读取范围，A1 表示法；可带 sheet 前缀，如 Sheet1!A1:D10
- --no-header <Bool>: 首行不作为表头，自动生成 col1/col2/...

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
