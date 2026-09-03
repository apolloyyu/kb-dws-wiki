# dws sheet cond-format list

kind: command
completeness: full
usage: dws sheet cond-format list
description: 获取条件格式规则
example: dws sheet cond-format list --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_cond_format.go:14
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --rule-id <String>: 条件格式规则 ID (可选，不传则返回全部)

## Related
- dws sheet cond-format create
- dws sheet cond-format delete
- dws sheet cond-format update
