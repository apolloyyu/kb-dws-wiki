# dws sheet add-dimension

kind: command
completeness: full
usage: dws sheet add-dimension
description: 在末尾追加空行或空列
example: dws sheet add-dimension --node NODE_ID --sheet-id SHEET_ID --dimension ROWS --length 5
source: internal/helpers/sheet_dimension.go:228
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --dimension <String>: 维度类型: ROWS 或 COLUMNS (必填)
- --length <Int>: 追加数量，正整数 (必填)

## Related
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
- dws sheet cond-format
