# dws doc create

kind: command
completeness: partial
usage: dws doc create
description: Create a new DingTalk Doc (document type) in a target folder or knowledge base.
example: dws doc create --name "项目周报"
use_when: When the agent needs a fresh DingTalk Doc to write into.
source: internal/helpers/doc.go:1593
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --name <String>: 文档名称 (必填)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID
- --content <String>: 文档初始内容（短文本字面量）；传 - 表示从 stdin 读取
- --content-file <String>: 从文件读取文档内容（UTF-8）。推荐长/多行/表格内容使用
- --content-format <String>: 内容格式: 默认为 markdown，可选 jsonml

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc delete
- dws doc download
- dws doc export
