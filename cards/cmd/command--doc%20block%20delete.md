# dws doc block delete

kind: command
completeness: full
usage: dws doc block delete
description: Delete a block from a DingTalk Doc by block ID.
example: dws doc block delete --node DOC_ID --block-id BLOCK_ID --yes
use_when: When the agent is editing a document and needs to remove a specific paragraph, table, or other block.
source: internal/helpers/doc.go:2401
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --block-id <String>: 目标块 ID (必填); 支持逗号分隔一次删除多个, 如 a,b,c, 单次最多 50 个

## Related
- dws doc block insert
- dws doc block list
- dws doc block update
