# dws aitable template search

kind: command
completeness: full
description: Search the AI table template gallery by keyword.
use_when: When the agent needs to suggest or bootstrap from an existing Base template rather than building from scratch.
source: internal/helpers/aitable.go:1765
visible_flags: 2

## Flags
- --query <String>: Base 名称关键词，建议至少 2 个字符 (必填)
- --cursor <String>: 分页游标，首次不传

## Related
- none
