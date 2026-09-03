# dws sheet filter delete

kind: command
completeness: full
description: 删除全局筛选
source: internal/helpers/sheet_filter_view.go:291
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)

## Related
- dws sheet filter clear-criteria
- dws sheet filter create
- dws sheet filter get
- dws sheet filter sort
- dws sheet filter update
