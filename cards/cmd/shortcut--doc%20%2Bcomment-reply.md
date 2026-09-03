# dws doc +comment-reply

kind: shortcut
completeness: full
usage: dws doc +comment-reply
description: 回复文档中的一条评论
source: internal/shortcut/doc/doc.go:531
visible_flags: 5

## Flags
- --node <String>: 文档 ID 或 URL
- --content <String>: 回复文字内容 (表情回复时填表情名称)
- --comment-key <String>: 被回复评论的 commentKey (从 list/create 获取)
- --emoji <Bool>: 作为表情贴图回复
- --mention <StringSlice>: 被 @ 的用户 uid，多个值用逗号分隔；不要传 JSON 数组

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
