# dws sheet comment update

kind: command
completeness: full
usage: dws sheet comment update
description: 更新单元格评论
example: dws sheet comment update --node <SHEET_ID> --comment-key <COMMENT_KEY> --content "已按最新数据修正"
source: internal/helpers/sheet_comment.go:202
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --comment-key <String>: 待更新评论的 commentKey (必填)
- --content <String>: 更新后的评论内容 (必填)

## Related
- dws sheet comment create
- dws sheet comment delete
- dws sheet comment list
- dws sheet comment reply
