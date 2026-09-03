# dws sheet move-dimension

kind: command
completeness: full
usage: dws sheet move-dimension
description: 移动行或列到指定位置/调整顺序
example: dws sheet move-dimension --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_dimension.go:132
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --dimension <String>: 维度类型: ROWS 或 COLUMNS (必填)
- --start-index <String>: 源起始位置，A1 表示法 (必填)
- --end-index <String>: 源结束位置，A1 表示法 (必填)
- --destination-index <String>: 目标位置，A1 表示法 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
