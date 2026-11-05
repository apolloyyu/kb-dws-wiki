# dws doc block update

kind: command
completeness: partial
usage: dws doc block update
description: Update the content or properties of an existing block in a DingTalk Doc.
example: dws doc block update --node DOC_ID --block-id BLOCK_ID --content "新内容"
use_when: When the agent amends a specific paragraph or element without rewriting the whole document.
source: internal/helpers/doc.go:2469
visible_flags: 9
partial_reason: unverified_flags

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --block-id <String>: 目标块 ID；与起止范围互斥
- --start-block-id <String>: 顶层闭区间起点 UUID；须与 --end-block-id 成对
- --end-block-id <String>: 顶层闭区间终点 UUID（含）；须与 --start-block-id 成对
- --heading <String>: 快捷: 标题文本
- --level <Int>: 标题级别 1-6 (配合 --heading)
- --element <String>: 块元素 JSON (高级)
- --content-format <String>: 输入格式: element（默认）、markdown、jsonml；序列用 --jsonml-nodes
- … 1 more; use dwsdoc cmd/short for full flags

## Related
- dws doc block delete
- dws doc block insert
- dws doc block list
