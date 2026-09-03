# dws markdown diff

kind: command
completeness: full
description: 比较 Markdown 内容差异
source: internal/helpers/markdown_diff.go:194
visible_flags: 5

## Flags
- --node <String>: 文件 ID (dentryUuid) 或 URL (必填)
- --version <Int>: 左侧历史版本号（可选；显式传入时必须为正整数，不传=最新版本）
- --version2 <Int>: 右侧历史版本号（可选；显式传入时必须为正整数，不传=最新版本；不能与 --file 同时使用）
- --file <String>: 本地 .md 文件路径 (可选，指定后进入 remote_vs_local 模式)
- --context <Int>: diff 上下文行数（必须为非负整数，默认 3）

## Related
- dws markdown comment
- dws markdown create
- dws markdown fetch
- dws markdown overwrite
- dws markdown patch
