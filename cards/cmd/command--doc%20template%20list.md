# dws doc template list

kind: command
completeness: full
description: 遍历文件列表
source: internal/helpers/doc.go:1331
visible_flags: 4

## Flags
- --folder <String>: 文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 知识库 ID
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标 (从上次结果的 nextPageToken 获取)

## Related
- dws doc template apply
- dws doc template search
