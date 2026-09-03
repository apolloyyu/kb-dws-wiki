# dws sheet pivot-table update

kind: command
completeness: full
usage: dws sheet pivot-table update
description: 更新透视表配置
example: dws sheet pivot-table update --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_pivot_table.go:265
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --pivot-table-id <String>: 透视表 ID (必填)
- --properties <String>: 需要更新的透视表配置 JSON 或 @文件路径 (必填)

## Related
- dws sheet pivot-table create
- dws sheet pivot-table delete
- dws sheet pivot-table list
