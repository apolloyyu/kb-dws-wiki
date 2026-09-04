# dws doc comment reply

kind: command
completeness: full
usage: dws doc comment reply
description: Reply to an existing comment on a DingTalk Doc.
example: dws doc comment reply --node DOC_ID --comment-key COMMENT_KEY --content "同意"
use_when: When the agent responds to a reviewer's comment inline rather than starting a new thread.
source: internal/helpers/doc.go:3262
visible_flags: 6

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --content <String>: 回复的文字内容，表情回复时填写表情名称 (必填)
- --comment-key <String>: 被回复评论的 commentKey，格式: {13位毫秒时间戳}{32位UUID}，可从 list/create 结果获取 (必填)
- --emoji <Bool>: 设为 true 时作为表情贴图回复 (默认 false)
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔
- --mentioned-open-conversation-id <StringSlice>: 被 @ 的群 openConversationId，可重复指定或逗号分隔

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment list
- dws doc comment update
