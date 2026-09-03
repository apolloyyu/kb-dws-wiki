# dws doc +template-apply

kind: shortcut
completeness: full
usage: dws doc +template-apply
description: 使用指定模板创建新文档
source: internal/shortcut/doc/doc.go:1019
visible_flags: 4

## Flags
- --template-id <String>: 模板 ID
- --name <String>: 新文档名称 (可选)
- --folder <String>: 目标文件夹 ID (可选)
- --workspace <String>: 知识库 ID (可选)

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
