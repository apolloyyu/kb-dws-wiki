# dws doc block update

kind: command
completeness: partial
usage: dws doc block update
description: Update the content or properties of an existing block in a DingTalk Doc.
example: dws doc block update --node DOC_ID --block-id BLOCK_ID --content "新内容"
use_when: When the agent amends a specific paragraph or element without rewriting the whole document.
source: internal/helpers/doc.go:2313
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --block-id <String>: 目标块 ID (必填)
- --heading <String>: 快捷: 标题文本
- --level <Int>: 标题级别 1-6 (配合 --heading)
- --element <String>: 块元素 JSON (高级)
- --content-format <String>: 输入格式: 默认为 element，可选 jsonml

## Related
- dws doc block delete
- dws doc block insert
- dws doc block list
