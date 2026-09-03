# dws doc comment create

kind: command
completeness: full
usage: dws doc comment create
description: Create a document-level comment on a DingTalk Doc.
example: dws doc comment create --node DOC_ID --content "这里需要修改"
use_when: When the agent leaves feedback or follow-up notes that apply to the entire document.
source: internal/helpers/doc.go:3167
visible_flags: 4

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --content <String>: 评论的文字内容，纯文本 (必填)
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔
- --mentioned-open-conversation-id <StringSlice>: 被 @ 的群 openConversationId，可重复指定或逗号分隔

## Related
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment list
- dws doc comment reply
- dws doc comment update
