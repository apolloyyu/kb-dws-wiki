# dws html fetch

kind: command
completeness: partial
usage: dws html fetch
description: 获取 HTML 文件内容
example: dws html fetch --node <dentryUuid>
source: internal/helpers/markdown.go:677
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --node <String>: 文件 ID (dentryUuid/nodeId) (必填)
- --space-id <String>: 文件所属钉盘空间 ID (可选，与 --workspace 互斥)
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --output <String>: 本地保存路径（文件或已有目录；不传则仅输出内容）

## Related
- dws html create
- dws html overwrite
- dws html patch
