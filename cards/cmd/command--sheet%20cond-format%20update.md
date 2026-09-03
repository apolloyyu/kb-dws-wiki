# dws sheet cond-format update

kind: command
completeness: full
description: 更新条件格式规则
source: internal/helpers/sheet_cond_format.go:232
visible_flags: 7

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --rule-id <String>: 条件格式规则 ID (必填)
- --ranges <String>: A1:E10
- --condition <String>: —
- --cell-style <String>: —
- --data-bar-style <String>: —

## Related
- dws sheet cond-format create
- dws sheet cond-format delete
- dws sheet cond-format list
