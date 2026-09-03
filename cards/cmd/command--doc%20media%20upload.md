# dws doc media upload

kind: command
completeness: full
description: 上传文件到钉钉文档或钉钉知识库
source: internal/helpers/doc.go:1994
visible_flags: 5

## Flags
- --file <String>: 本地文件路径 (必填)
- --name <String>: 文件显示名称 (默认使用文件名)
- --folder <String>: 目标文档文件夹 nodeId 或 alidocs 文件夹 URL；不要传 drive dentryId/parent-id
- --workspace <String>: 目标知识库 ID
- --convert <Bool>: 是否转换为钉钉在线文档

## Related
- dws doc media download
- dws doc media insert
