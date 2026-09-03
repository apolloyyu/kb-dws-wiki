# dws sheet +list-sheets

kind: shortcut
completeness: full
usage: dws sheet +list-sheets
description: 严格列出在线电子表格的工作表，并可按完整标题精确筛选
source: internal/shortcut/sheet/sheet.go:40
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL；--node 去除空白后不能为空
- --title <String>: 按完整工作表标题精确筛选（区分大小写）；显式传入时去除空白后不能为空

## Related
- dws sheet +read
