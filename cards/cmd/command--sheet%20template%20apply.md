# dws sheet template apply

kind: command
completeness: full
description: 应用表格模板
source: internal/helpers/sheet_template.go:137
visible_flags: 4

## Flags
- --template-id <String>: 模板 ID (必填)
- --name <String>: 新表格文档名称 (可选)
- --folder <String>: 目标文件夹 ID (可选)
- --workspace <String>: 知识库 ID (可选)

## Related
- dws sheet template list
- dws sheet template search
