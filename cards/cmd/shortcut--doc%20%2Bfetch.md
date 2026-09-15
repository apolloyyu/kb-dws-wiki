# dws doc +fetch

kind: shortcut
completeness: partial
usage: dws doc +fetch
description: 读取完整或局部文档内容，并按 detail 控制保真度
source: internal/shortcut/doc/content_shortcuts.go:220
visible_flags: 17
partial_reason: too_many_flags:17

## Flags
- --include-comments <Bool>: 同时读取全文评论，自动翻页；评论范围始终是整篇文档，最多1000条，超限报不完整
- --context-unit <String>: —
- --regex <Bool>: keyword+blocks模式使用RE2正则；非法正则在请求前拒绝
- --node <String>: 文档 ID 或 URL；
- --query <String>: 文档标题或关键词；跨页唯一解析后读取；
- --detail <String>: —
- --scope <String>: —
- --start-block-id <String>: range/section 起始块 ID
- … 9 more; use dwsdoc cmd/short for full flags

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
