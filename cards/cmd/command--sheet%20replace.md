# dws sheet replace

kind: command
completeness: full
usage: dws sheet replace
description: 查找替换/批量替换/精确匹配替换/正则替换文本
example: dws sheet replace --node NODE_ID --sheet-id SHEET_ID --find "旧文本" --replacement "新文本"
source: internal/helpers/sheet_data.go:123
visible_flags: 10

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --find <String>: 查找文本 (必填)
- --replacement <String>: 替换文本 (必填，可为空字符串表示删除)
- --range <String>: 替换范围，A1 表示法 (如 A1:D100)
- --match-case <Bool>: 区分大小写 (默认 false)
- --match-entire-cell <Bool>: 完整单元格匹配
- --use-regexp <Bool>: 启用正则表达式匹配
- --match-formula <Bool>: 在公式文本中查找替换（默认 false）
- --include-hidden <Bool>: 包含隐藏行/列

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
