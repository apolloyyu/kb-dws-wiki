# dws doc upload

kind: command
completeness: full
usage: dws doc upload
description: Obtain upload credentials and URL for uploading a local file as an attachment into DingTalk Docs or a knowledge base.
example: dws doc upload --file ./report.pdf
use_when: When the agent needs to stage a local file for attachment into the DingTalk Docs system.
source: internal/helpers/doc.go:1996
visible_flags: 5

## Flags
- --file <String>: 本地文件路径 (必填)
- --name <String>: 文件显示名称 (默认使用文件名)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID
- --convert <Bool>: 是否转换为钉钉在线文档

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc delete
- dws doc download
