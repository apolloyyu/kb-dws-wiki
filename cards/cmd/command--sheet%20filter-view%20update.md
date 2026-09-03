# dws sheet filter-view update

kind: command
completeness: full
description: 批量更新筛选条件
source: internal/helpers/sheet_filter_view.go:341
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --criteria <String>: 筛选条件 JSON 数组 (必填)

## Related
- dws sheet filter-view create
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
