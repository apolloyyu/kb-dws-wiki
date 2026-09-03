# dws devdoc article search

kind: command
completeness: full
description: Search the DingTalk Open Platform documentation by keyword.
use_when: When the agent needs authoritative API reference or guides to answer a developer question.
source: internal/helpers/devdoc.go:48
visible_flags: 3

## Flags
- --query <String>: 搜索关键词 (必填)
- --page <String>: 页码，默认 1
- --size <String>: 每页数量，默认 10

## Related
- none
