# dws doc template search

kind: command
completeness: full
usage: dws doc template search
description: 搜索文档模板
example: dws doc template search --query "周报"
source: internal/helpers/doc.go:4649
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --source <String>: 模板来源: MY(我的模版)/PUBLIC(公开模版)，不传默认 MY
- --limit <Int>: 返回数量上限
- --cursor <String>: 分页游标

## Related
- dws doc template apply
- dws doc template list
