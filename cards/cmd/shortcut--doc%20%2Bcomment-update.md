# dws doc +comment-update

kind: shortcut
completeness: full
usage: dws doc +comment-update
description: 更新指定文档评论正文和 mention
source: internal/shortcut/doc/review_shortcuts.go:52
visible_flags: 4

## Flags
- --node <String>: 文档 ID 或 URL
- --comment-key <String>: 评论 commentKey
- --content <String>: 更新后的评论正文
- --mention <StringSlice>: 被 @ 的用户 uid，多个值用逗号分隔；不要传 JSON 数组

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
