# dws smart +doc-append

kind: shortcut
completeness: full
usage: dws smart +doc-append
description: 在文档末尾追加一段文本（安全追加，不改动原有内容）
source: internal/shortcut/smart/doc_append.go:42
visible_flags: 2

## Flags
- --doc <String>: 文档 documentId / nodeId（或文档 URL/token）
- --content <String>: 要追加到文档末尾的文本

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
