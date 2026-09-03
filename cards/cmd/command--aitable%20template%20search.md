# dws aitable template search

kind: command
completeness: full
usage: dws aitable template search
description: Search the AI table template gallery by keyword.
example: dws aitable template search --query "项目管理"
use_when: When the agent needs to suggest or bootstrap from an existing Base template rather than building from scratch.
source: internal/helpers/aitable.go:3652
visible_flags: 3

## Flags
- --query <String>: 模板名称关键词 (必填)
- --limit <Int>: 每页返回数量。默认 10，最大 30
- --cursor <String>: 分页游标。首次请求不传；后续请原样传入上次返回的 nextCursor

## Related
- none
