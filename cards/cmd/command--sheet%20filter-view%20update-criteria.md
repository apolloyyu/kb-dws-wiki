# dws sheet filter-view update-criteria

kind: command
completeness: full
usage: dws sheet filter-view update-criteria
description: 更新筛选视图列条件
example: dws sheet filter-view update-criteria --node NODE_ID --sheet-id SHEET_ID --filter-view-id FV_ID
source: internal/helpers/sheet_filter_view.go:848
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --filter-view-id <String>: 筛选视图 ID (必填)
- --column <Int>: 列偏移量，从 0 开始 (必填)
- --filter-criteria <String>: 筛选条件，JSON 对象 (必填)

## Related
- dws sheet filter-view create
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
