# dws sheet filter-view get-criteria

kind: command
completeness: full
usage: dws sheet filter-view get-criteria
description: 获取单列筛选条件
example: dws sheet filter-view get-criteria --node NODE_ID --sheet-id SHEET_ID --filter-view-id FV_ID --column 0
source: internal/helpers/sheet_filter_view.go:1142
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --filter-view-id <String>: 筛选视图 ID (必填)
- --column <Int>: 列偏移量，从 0 开始 (必填)

## Related
- dws sheet filter-view create
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view info
- dws sheet filter-view list
- dws sheet filter-view list-criteria
