# dws sheet comment reply

kind: command
completeness: full
description: 回复单元格评论
source: internal/helpers/sheet_comment.go:139
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --content <String>: 回复内容 (必填)
- --comment-key <String>: 被回复评论的 commentKey (必填)
- --emoji <Bool>: 作为表情贴图回复
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔

## Related
- dws sheet comment create
- dws sheet comment delete
- dws sheet comment list
- dws sheet comment update
