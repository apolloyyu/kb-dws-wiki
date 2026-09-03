# dws sheet filter-view create

kind: command
completeness: full
description: 创建全局筛选
source: internal/helpers/sheet_filter_view.go:218
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 筛选范围，A1 表示法，须包含表头行 (必填)
- --criteria <String>: 筛选条件 JSON 数组 (可选)

## Related
- dws sheet filter-view delete
- dws sheet filter-view delete-criteria
- dws sheet filter-view get-criteria
- dws sheet filter-view info
- dws sheet filter-view list
- dws sheet filter-view list-criteria
