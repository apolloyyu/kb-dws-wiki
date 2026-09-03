# dws doc info

kind: command
completeness: full
usage: dws doc info
description: Retrieve metadata for a document or file (title, type, owner, path, permissions).
example: dws doc info --node DOC_ID
use_when: When the agent needs descriptive info about a node without fetching its full content.
source: internal/helpers/doc.go:1401
visible_flags: 1

## Flags
- --node <String>: 文档 ID 或 URL (必填)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
