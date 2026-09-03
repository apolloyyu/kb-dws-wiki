# dws devdoc article search

kind: command
completeness: partial
usage: dws devdoc article search [keyword]
description: Search the DingTalk Open Platform documentation by keyword.
example: dws devdoc article search "MCP"
use_when: When the agent needs authoritative API reference or guides to answer a developer question.
source: internal/helpers/devdoc.go:48
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --query <String>: 搜索关键词 (必填)
- --page <String>: 页码，默认 1
- --size <String>: 每页数量，默认 10

## Related
- none
