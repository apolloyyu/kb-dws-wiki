# dws doc +move

kind: shortcut
completeness: full
description: 移动文档/文件到指定文件夹或知识库
source: internal/shortcut/doc/doc.go:372
visible_flags: 3

## Flags
- --node <String>: 文档/文件 ID 或 URL
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL
- --workspace <String>: 目标知识库 ID

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
