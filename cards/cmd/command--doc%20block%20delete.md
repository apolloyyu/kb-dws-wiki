# dws doc block delete

kind: command
completeness: full
description: Delete a block from a DingTalk Doc by block ID.
use_when: When the agent is editing a document and needs to remove a specific paragraph, table, or other block.
source: internal/helpers/doc.go:2399
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --block-id <String>: 目标块 ID (必填)

## Related
- dws doc block insert
- dws doc block list
- dws doc block update
