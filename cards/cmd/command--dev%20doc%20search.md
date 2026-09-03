# dws dev doc search

kind: command
completeness: partial
usage: dws dev doc search [keyword]
description: 搜索开放平台文档
example: dws dev doc search "MCP"
source: internal/helpers/devdoc.go:139
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --query <String>: 搜索关键词 (必填)
- --page <String>: 页码，默认 1
- --size <String>: 每页数量，默认 10

## Related
- none
