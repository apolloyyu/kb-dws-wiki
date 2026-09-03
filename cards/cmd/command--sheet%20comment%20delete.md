# dws sheet comment delete

kind: command
completeness: full
usage: dws sheet comment delete
description: 删除单元格评论
example: dws sheet comment delete --node <SHEET_ID> --comment-key <COMMENT_KEY> --yes
source: internal/helpers/sheet_comment.go:252
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --comment-key <String>: 待删除评论的 commentKey (必填)

## Related
- dws sheet comment create
- dws sheet comment list
- dws sheet comment reply
- dws sheet comment update
