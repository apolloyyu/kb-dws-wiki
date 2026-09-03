# dws sheet table-put

kind: command
completeness: full
usage: dws sheet table-put
description: 写入结构化 table 数据
example: dws sheet table-put --node NODE_ID
source: internal/helpers/sheet_table.go:96
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheets <String>: sheet table JSON、@文件路径 或 - 表示 stdin (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
