# dws doc comment update

kind: command
completeness: full
usage: dws doc comment update
description: 更新文档评论
example: dws doc comment update --node DOC_ID --comment-key COMMENT_KEY --content "已按最新数据修正"
source: internal/helpers/doc.go:3343
visible_flags: 5

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --comment-key <String>: 待更新评论的 commentKey，可从 list/create/create-inline 结果获取 (必填)
- --content <String>: 更新后的评论文字内容，纯文本 (必填)
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔
- --mentioned-open-conversation-id <StringSlice>: 被 @ 的群 openConversationId，可重复指定或逗号分隔

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment list
- dws doc comment reply
