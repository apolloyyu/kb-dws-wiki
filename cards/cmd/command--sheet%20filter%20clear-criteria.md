# dws sheet filter clear-criteria

kind: command
completeness: full
usage: dws sheet filter clear-criteria
description: 清除单列筛选条件
example: dws sheet filter clear-criteria --node NODE_ID --sheet-id SHEET_ID --column 1
source: internal/helpers/sheet_filter_view.go:411
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --column <Int>: 列偏移量，从 0 开始 (必填)

## Related
- dws sheet filter create
- dws sheet filter delete
- dws sheet filter get
- dws sheet filter sort
- dws sheet filter update
