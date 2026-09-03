# dws aitable search

kind: command
completeness: full
description: 搜索 AI 表格
source: internal/helpers/aitable.go:1765
visible_flags: 2

## Flags
- --query <String>: Base 名称关键词，建议至少 2 个字符 (必填)
- --cursor <String>: 分页游标，首次不传

## Related
- dws aitable create
- dws aitable info
- dws aitable list
