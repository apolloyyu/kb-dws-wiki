# dws doc block list

kind: command
completeness: full
usage: dws doc block list
description: List the blocks of a DingTalk Doc with their IDs, types, and content.
example: dws doc block list --node DOC_ID
use_when: When the agent needs the structured block tree of a doc before modifying specific blocks.
source: internal/helpers/doc.go:2102
visible_flags: 6

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --start-index <Int>: 起始位置 (从 0 开始)
- --end-index <Int>: 终止位置 (含)
- --block-type <String>: 按块类型过滤
- --content-format <String>: 输出格式: 默认为 element，可选 jsonml（返回 JSONML 节点数组）
- --block-id <String>: 指定块 UUID（content-format=jsonml 时读取完整子树）

## Related
- dws doc block delete
- dws doc block insert
- dws doc block update
