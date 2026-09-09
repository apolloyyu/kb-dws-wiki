# dws doc file create

kind: command
completeness: full
usage: dws doc file create
description: Create a new file node of a given type (doc, sheet, mind map, whiteboard, AI table, etc.) in a target folder.
example: dws doc file create --name "项目周报" --type adoc
use_when: When the agent provisions any non-plain-document file type inside DingTalk Docs.
source: internal/helpers/doc.go:1860
visible_flags: 4

## Flags
- --name <String>: 文件名称 (必填)
- --type <String>: 文件类型: adoc/axls/appt/adraw/amind/able/folder (必填)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID 或 URL

## Related
- none
