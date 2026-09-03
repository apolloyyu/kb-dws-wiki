# dws doc media download

kind: command
completeness: full
description: 下载文件
source: internal/helpers/doc.go:2045
visible_flags: 2

## Flags
- --node <String> required: 文件节点 ID 或 URL (必填)
- --output <String> required: 本地保存路径 (文件路径或目录)

## Related
- dws doc media insert
- dws doc media upload
