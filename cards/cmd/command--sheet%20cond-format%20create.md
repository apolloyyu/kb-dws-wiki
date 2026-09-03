# dws sheet cond-format create

kind: command
completeness: full
description: 创建条件格式规则
source: internal/helpers/sheet_cond_format.go:75
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --ranges <String>: A1:E10
- --condition <String>: 80
- --cell-style <String>: bold
- --data-bar-style <String>: isGradient

## Related
- dws sheet cond-format delete
- dws sheet cond-format list
- dws sheet cond-format update
