# dws drive comment create

kind: command
completeness: partial
usage: dws drive comment create
description: —
source: internal/helpers/file_comment.go:150
visible_flags: 1
partial_reason: unverified_flags,missing_description

## Flags
- --content <String> required: 全文评论内容，纯文本且 UTF-16 长度不超过 2099

## Related
- dws drive comment list
