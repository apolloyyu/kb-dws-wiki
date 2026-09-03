# dws sheet delete-dimension

kind: command
completeness: full
description: 删除指定位置的行或列
source: internal/helpers/sheet_dimension.go:434
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --dimension <String>: 删除维度: ROWS 或 COLUMNS (必填)
- --position <String>: 删除起始位置，A1 表示法 (必填)。ROWS 时为行号如 \"3\"；COLUMNS 时为列字母如 \"A\"
- --length <String>: 删除数量，正整数 (必填)，最大 5000

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
