# dws sheet insert-dimension

kind: command
completeness: full
description: 在指定位置插入行或列
source: internal/helpers/sheet_dimension.go:42
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --dimension <String>: 插入维度: ROWS 或 COLUMNS (必填)
- --position <String>: 插入位置，A1 表示法 (必填)。ROWS 时为行号如 \"3\"；COLUMNS 时为列字母如 \"A\"
- --length <String>: 插入数量，正整数 (必填)，最大 5000

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
