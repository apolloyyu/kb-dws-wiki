# dws sheet cond-format delete

kind: command
completeness: full
description: 删除条件格式规则
source: internal/helpers/sheet_cond_format.go:351
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --rule-id <String>: 条件格式规则 ID (必填)
- --yes <Bool>: 确认删除（危险操作，必须用户同意后才加此标志）

## Related
- dws sheet cond-format create
- dws sheet cond-format list
- dws sheet cond-format update
