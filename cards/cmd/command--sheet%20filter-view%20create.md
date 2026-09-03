# dws sheet filter-view create

kind: command
completeness: full
usage: dws sheet filter-view create
description: 创建筛选视图
example: dws sheet filter-view create --node NODE_ID --sheet-id SHEET_ID --name "我的视图" --range "A1:E10"
source: internal/helpers/sheet_filter_view.go:596
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --name <String>: 筛选视图名称 (必填)
- --range <String>: 筛选视图范围，A1 表示法，如 A1:E10 (必填)
- --criteria <String>: 筛选条件，JSON 数组 (可选)

## Related
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
- dws sheet filter-view list-criteria
