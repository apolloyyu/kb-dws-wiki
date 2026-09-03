# dws sheet filter sort

kind: command
completeness: full
description: 筛选排序
source: internal/helpers/sheet_filter_view.go:467
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --column <Int>: 排序列偏移量，从 0 开始 (必填)
- --ascending <Bool>: 是否升序，默认 true

## Related
- dws sheet filter clear-criteria
- dws sheet filter create
- dws sheet filter delete
- dws sheet filter get
- dws sheet filter update
