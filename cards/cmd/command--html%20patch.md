# dws html patch

kind: command
completeness: partial
usage: dws html patch
description: 局部替换 HTML 文本
example: dws html patch --node <id> --pattern old --content new --dry-run
source: internal/helpers/markdown.go:816
visible_flags: 7
partial_reason: unverified_flags

## Flags
- --node <String>: 目标文件 ID (必填)
- --pattern <String>: 要匹配的文本或正则表达式 (必填)
- --content <String>: 替换内容 (必填)
- --regex <Bool>: 使用 RE2 正则匹配
- --space-id <String>: 钉盘空间 ID (可选，与 --workspace 互斥)
- --workspace <String>: 文档空间/知识库 ID (可选，与 --space-id 互斥)
- --dry-run <Bool>: 下载当前内容并预览替换差异，不写入

## Related
- dws html create
- dws html fetch
- dws html overwrite
