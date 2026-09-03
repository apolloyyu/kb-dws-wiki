# dws doc template apply

kind: command
completeness: full
description: 应用文档模板
source: internal/helpers/doc.go:4718
visible_flags: 4

## Flags
- --template-id <String>: 模板 ID (必填)
- --name <String>: 新文档名称 (可选)
- --folder <String>: 目标文件夹 ID (可选)
- --workspace <String>: 知识库 ID (可选)

## Related
- dws doc template list
- dws doc template search
