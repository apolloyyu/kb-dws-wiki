# dws doc block insert

kind: command
completeness: partial
usage: dws doc block insert
description: Insert a new block (paragraph, table, image, etc.) into a DingTalk Doc at a given position.
example: dws doc block insert --node DOC_ID --content "这是一段文字"
use_when: When the agent is programmatically assembling or editing a document's content.
source: internal/helpers/doc.go:2329
visible_flags: 10
partial_reason: unverified_flags

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --heading <String>: 快捷: 标题文本
- --level <Int>: 标题级别 1-6 (配合 --heading)
- --element <String>: 块元素 JSON (高级)
- --index <Int>: Markdown/jsonml-nodes 顶层插入位置（0 到块数量）；ref-block 优先；旧单节点 jsonml 无参照块仍追加末尾
- --where <String>: 插入方向: before / after (默认 after)
- --ref-block <String>: 参照块 ID (优先级高于 --index)
- --content-format <String>: 输入格式: element（默认）、markdown、jsonml；序列用 --jsonml-nodes
- … 2 more; use dwsdoc cmd/short for full flags

## Related
- dws doc block delete
- dws doc block list
- dws doc block update
