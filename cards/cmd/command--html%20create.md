# dws html create

kind: command
completeness: full
usage: dws html create
description: 创建原生 .html 文件
example: dws html create --name index.html --content "<h1>Hello</h1>"
source: internal/helpers/markdown.go:606
visible_flags: 6

## Flags
- --name <String>: 文件名，必须以 .html/.htm 结尾（--content 模式必填）
- --content <String>: HTML 内容；支持字面值、@file、-（stdin）；与 --file 互斥
- --file <String>: 本地 .html/.htm 文件路径；与 --content 互斥
- --folder <String>: 父文件夹 ID（未指定空间参数时自动识别所在域）
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --space-id <String>: 钉盘空间 ID (可选，与 --workspace 互斥)

## Related
- dws html fetch
- dws html overwrite
- dws html patch
