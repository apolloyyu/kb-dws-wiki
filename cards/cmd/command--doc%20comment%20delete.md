# dws doc comment delete

kind: command
completeness: full
usage: dws doc comment delete
description: 删除文档评论
example: dws doc comment delete --node DOC_ID --comment-key COMMENT_KEY --yes
source: internal/helpers/doc.go:3417
visible_flags: 2

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --comment-key <String>: 待删除评论的 commentKey，可从 list/create/create-inline 结果获取 (必填)

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment list
- dws doc comment reply
- dws doc comment update
