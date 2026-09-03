# dws doc search

kind: command
completeness: full
description: Search DingTalk Docs the user can access by keyword.
use_when: When the agent needs to locate a document by title or content before reading or editing it.
source: internal/helpers/devdoc.go:48
visible_flags: 3

## Flags
- --query <String>: 搜索关键词 (必填)
- --page <String>: 页码，默认 1
- --size <String>: 每页数量，默认 10

## Related
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
- dws doc export
- dws doc import
