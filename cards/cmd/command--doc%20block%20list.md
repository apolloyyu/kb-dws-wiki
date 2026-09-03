# dws doc block list

kind: command
completeness: full
description: List the blocks of a DingTalk Doc with their IDs, types, and content.
use_when: When the agent needs the structured block tree of a doc before modifying specific blocks.
source: internal/helpers/doc.go:1331
visible_flags: 4

## Flags
- --folder <String>: 文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 知识库 ID
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (从上次结果的 nextPageToken 获取)

## Related
- dws doc block delete
- dws doc block insert
- dws doc block update
