# dws sheet filter get

kind: command
completeness: full
usage: dws sheet filter get
description: 获取全局筛选信息
example: dws sheet filter get --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_filter_view.go:169
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)

## Related
- dws sheet filter clear-criteria
- dws sheet filter create
- dws sheet filter delete
- dws sheet filter sort
- dws sheet filter update
