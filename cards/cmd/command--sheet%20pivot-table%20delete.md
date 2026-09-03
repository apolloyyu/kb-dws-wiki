# dws sheet pivot-table delete

kind: command
completeness: full
description: [危险] 删除透视表
source: internal/helpers/sheet_pivot_table.go:322
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --pivot-table-id <String>: 透视表 ID (必填)

## Related
- dws sheet pivot-table create
- dws sheet pivot-table list
- dws sheet pivot-table update
