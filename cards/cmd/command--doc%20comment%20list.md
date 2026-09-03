# dws doc comment list

kind: command
completeness: full
description: List comments on a DingTalk Doc, including replies.
use_when: When the agent is reviewing outstanding feedback or summarizing comment threads.
source: internal/helpers/doc.go:1331
visible_flags: 4

## Flags
- --folder <String>: 文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 知识库 ID
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (从上次结果的 nextPageToken 获取)

## Related
- dws doc comment create
- dws doc comment create-inline
- dws doc comment delete
- dws doc comment reply
- dws doc comment update
