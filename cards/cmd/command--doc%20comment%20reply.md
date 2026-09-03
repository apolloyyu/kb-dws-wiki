# dws doc comment reply

kind: command
completeness: full
description: Reply to an existing comment on a DingTalk Doc.
use_when: When the agent responds to a reviewer's comment inline rather than starting a new thread.
source: internal/helpers/doc.go:3245
visible_flags: 5

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --content <String>: 回复的文字内容，表情回复时填写表情名称 (必填)
- --comment-key <String>: 被回复评论的 commentKey，格式: {13位毫秒时间戳}{32位UUID}，可从 list/create 结果获取 (必填)
- --emoji <Bool>: 设为 true 时作为表情贴图回复 (默认 false)
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment list
- dws doc comment update
