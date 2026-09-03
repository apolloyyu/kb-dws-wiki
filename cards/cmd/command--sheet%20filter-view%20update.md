# dws sheet filter-view update

kind: command
completeness: full
usage: dws sheet filter-view update
description: 更新筛选视图属性
example: dws sheet filter-view update --node NODE_ID --sheet-id SHEET_ID --filter-view-id FV_ID --name "新名称"
source: internal/helpers/sheet_filter_view.go:685
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --filter-view-id <String>: 筛选视图 ID (必填)
- --name <String>: 筛选视图新名称
- --range <String>: 筛选视图新范围，A1 表示法
- --criteria <String>: 筛选条件，JSON 数组

## Related
- dws sheet filter-view create
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
