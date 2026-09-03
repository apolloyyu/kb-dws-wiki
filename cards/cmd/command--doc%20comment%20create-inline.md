# dws doc comment create-inline

kind: command
completeness: full
usage: dws doc comment create-inline
description: Create an inline (anchored) comment on a specific text range within a DingTalk Doc.
example: dws doc comment create-inline --node DOC_ID --block-id BLOCK_ID --start 0 --end 10 --content "这里需要修改"
use_when: When the agent needs to attach feedback to a particular passage rather than the whole doc.
source: internal/helpers/doc.go:3472
visible_flags: 7

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --content <String>: 评论的文字内容，纯文本 (必填)
- --block-id <String>: 评论标记所在的块 ID，可通过 dws doc block list 获取 (必填)
- --start <Int>: 评论标记在块内文本中的起始字符偏移量，从 0 开始 (必填)
- --end <Int>: 评论标记在块内文本中的结束字符偏移量，必须大于 start (必填)
- --selected-text <String>: 选中文本的内容，填写后评论列表中会展示「引用原文：xxx」
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔

## Related
- dws doc comment create
- dws doc comment delete
- dws doc comment list
- dws doc comment reply
- dws doc comment update
