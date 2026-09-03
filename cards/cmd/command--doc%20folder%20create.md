# dws doc folder create

kind: command
completeness: full
description: Create a new folder inside a DingTalk Docs knowledge base or drive location.
use_when: When the agent organizes output into a fresh folder before writing files into it.
source: internal/helpers/doc.go:1591
visible_flags: 6

## Flags
- --name <String>: 文档名称 (必填)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID
- --content <String>: 文档初始内容（短文本字面量）；传 - 表示从 stdin 读取
- --content-file <String>: 从文件读取文档内容（UTF-8）。推荐长/多行/表格内容使用
- --content-format <String>: 内容格式: 默认为 markdown，可选 jsonml

## Related
- none
