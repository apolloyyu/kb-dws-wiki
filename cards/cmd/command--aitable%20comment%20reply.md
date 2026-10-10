# dws aitable comment reply

kind: command
completeness: partial
usage: dws aitable comment reply
description: —
source: internal/helpers/aitable_comment.go:137
visible_flags: 2
partial_reason: unverified_flags,missing_description

## Flags
- --content <String>: 纯文本评论正文；与 --rich-content 二选一
- --rich-content <String>: text/mention/image 有序节点 JSON 数组；与 --content 二选一

## Related
- dws aitable comment create
- dws aitable comment delete
- dws aitable comment list
- dws aitable comment update
