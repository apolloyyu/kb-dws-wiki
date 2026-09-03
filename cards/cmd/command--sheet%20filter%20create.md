# dws sheet filter create

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
- dws sheet filter clear-criteria
- dws sheet filter delete
- dws sheet filter get
- dws sheet filter sort
- dws sheet filter update
