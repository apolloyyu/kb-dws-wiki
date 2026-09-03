# dws markdown patch

kind: command
completeness: full
description: 局部替换 Markdown 文本
source: internal/helpers/markdown.go:603
visible_flags: 7

## Flags
- --node <String>: 目标文件 ID (必填)
- --pattern <String>: 要匹配的文本或正则表达式 (必填)
- --content <String>: 替换内容 (必填)
- --regex <Bool>: 使用 RE2 正则匹配
- --space-id <String>: 钉盘空间 ID (可选，与 --workspace 互斥)
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --dry-run <Bool>: 下载当前内容并预览替换差异，不写入

## Related
- dws markdown comment
- dws markdown create
- dws markdown diff
- dws markdown fetch
- dws markdown overwrite
