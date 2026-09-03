# dws sheet update-dimension

kind: command
completeness: full
description: 更新指定范围行/列属性（显隐、行高/列宽）
source: internal/helpers/sheet_dimension.go:520
visible_flags: 8

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --dimension <String>: 更新维度: ROWS 或 COLUMNS (必填)
- --start-index <String>: 起始位置，A1 表示法 (必填)。ROWS 时为行号如 \"3\"；COLUMNS 时为列字母如 \"A\"
- --length <String>: 更新数量，正整数 (必填)，最大 5000
- --hidden <Bool>: 是否隐藏 (true=隐藏, false=显示)
- --pixel-size <Int>: 行高或列宽（像素），ROWS 时为行高，COLUMNS 时为列宽
- --size-type <String>: 尺寸模式（对齐飞书）: pixel(默认,用 --pixel-size) / standard(恢复默认行高列宽) / auto(按内容自适应行高，仅 ROWS；列宽无此选项)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
