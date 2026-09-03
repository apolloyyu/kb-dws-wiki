# dws doc list

kind: command
completeness: full
usage: dws doc list
description: List the child nodes (files and subfolders) of a folder or knowledge base.
example: dws doc list
use_when: When the agent traverses the document hierarchy to find or enumerate items.
source: internal/helpers/doc.go:1331
visible_flags: 4

## Flags
- --folder <String>: 文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 知识库 ID
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (从上次结果的 nextPageToken 获取)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
