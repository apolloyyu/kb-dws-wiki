# dws sheet filter-view delete

kind: command
completeness: full
usage: dws sheet filter-view delete
description: 删除筛选视图
example: dws sheet filter-view delete --node NODE_ID --sheet-id SHEET_ID --filter-view-id FV_ID --yes
source: internal/helpers/sheet_filter_view.go:785
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --filter-view-id <String>: 筛选视图 ID (必填)

## Related
- dws sheet filter-view create
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
- dws sheet filter-view list-criteria
