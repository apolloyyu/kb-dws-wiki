# dws sheet version list

kind: command
completeness: full
usage: dws sheet version list
description: 查看表格历史版本列表
example: dws sheet version list --node SHEET_ID
source: internal/helpers/sheet_version.go:61
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --limit <Int>: 返回版本数量上限
- --cursor <String>: 分页游标

## Related
- dws sheet version revert
- dws sheet version save
