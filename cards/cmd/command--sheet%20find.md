# dws sheet find

kind: command
completeness: full
description: 在工作表中搜索单元格内容
source: internal/helpers/sheet_data.go:20
visible_flags: 9

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --query <String>: 搜索文本 (必填，别名: --find)
- --range <String>: 搜索范围，A1 表示法 (如 A1:D10)
- --match-case <Bool>: 区分大小写 (默认 true)
- --match-entire-cell <Bool>: 精确匹配整个单元格内容
- --use-regexp <Bool>: 启用正则表达式搜索
- --match-formula <Bool>: 搜索公式文本而非显示值
- --include-hidden <Bool>: 包含隐藏单元格

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
