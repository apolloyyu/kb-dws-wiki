# dws html overwrite

kind: command
completeness: partial
usage: dws html overwrite
description: 覆盖已有 HTML 文件
example: dws html overwrite --node <id> --content "<h1>New</h1>" --name index.html --dry-run
source: internal/helpers/markdown.go:745
visible_flags: 7
partial_reason: unverified_flags

## Flags
- --node <String>: 目标文件 ID (必填)
- --content <String>: 新内容；支持字面值、@file、-（stdin）；与 --file 互斥
- --file <String>: 本地 .html/.htm 文件路径；与 --content 互斥
- --name <String>: 文件名；省略时保留远程展示名
- --space-id <String>: 钉盘空间 ID (可选，与 --workspace 互斥)
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --dry-run <Bool>: 下载当前内容并预览覆盖差异，不写入

## Related
- dws html create
- dws html fetch
- dws html patch
