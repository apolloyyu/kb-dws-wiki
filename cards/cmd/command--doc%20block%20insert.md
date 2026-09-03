# dws doc block insert

kind: command
completeness: partial
usage: dws doc block insert
description: Insert a new block (paragraph, table, image, etc.) into a DingTalk Doc at a given position.
example: dws doc block insert --node DOC_ID --content "这是一段文字"
use_when: When the agent is programmatically assembling or editing a document's content.
source: internal/helpers/doc.go:2175
visible_flags: 9
partial_reason: unverified_flags

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --heading <String>: 快捷: 标题文本
- --level <Int>: 标题级别 1-6 (配合 --heading)
- --element <String>: 块元素 JSON (高级)
- --index <Int>: 参照位置索引 (从 0 开始)
- --where <String>: 插入方向: before / after (默认 after)
- --ref-block <String>: 参照块 ID (优先级高于 --index)
- --content-format <String>: 输入格式: 默认为 element，可选 jsonml
- … 1 more; use dwsdoc cmd/short for full flags

## Related
- dws doc block delete
- dws doc block list
- dws doc block update
