# dws doc +create-from-template

kind: shortcut
completeness: full
usage: dws doc +create-from-template
description: 使用已选定的 templateId 创建文档
source: internal/shortcut/doc/history_template_shortcuts.go:428
visible_flags: 6

## Flags
- --template-id <String>: 模板 ID
- --query <String>: 兼容入口：先搜索且仅唯一命中时创建；新的 Agent 流程应先调用 +template-search
- --source <String>: 模板来源
- --name <String>: 新文档名称
- --folder <String>: 目标文件夹 ID
- --workspace <String>: 目标知识库 ID

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
