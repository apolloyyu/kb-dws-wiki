# dws markdown create

kind: command
completeness: full
description: 创建原生 .md 文件
source: internal/helpers/markdown.go:237
visible_flags: 6

## Flags
- --name <String>: 文件名，必须以 .md 结尾（--content 模式必填）
- --content <String>: Markdown 内容；支持字面值、@file、-（stdin）；与 --file 互斥
- --file <String>: 本地 .md 文件路径；与 --content 互斥
- --folder <String>: 父文件夹 ID（未指定空间参数时自动识别所在域）
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --space-id <String>: 钉盘空间 ID (可选，与 --workspace 互斥)

## Related
- dws markdown comment
- dws markdown diff
- dws markdown fetch
- dws markdown overwrite
- dws markdown patch
