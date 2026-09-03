# dws sheet pivot-table list

kind: command
completeness: full
usage: dws sheet pivot-table list
description: 获取透视表列表或详情
example: dws sheet pivot-table list --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_pivot_table.go:143
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --pivot-table-id <String>: 透视表 ID (可选，不传则返回全部)

## Related
- dws sheet pivot-table create
- dws sheet pivot-table delete
- dws sheet pivot-table update
