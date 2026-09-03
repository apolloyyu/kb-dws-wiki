# dws doc template list

kind: command
completeness: full
usage: dws doc template list
description: 获取文档模板列表
example: dws doc template list
source: internal/helpers/doc.go:4593
visible_flags: 3

## Flags
- --source <String>: 模板来源: MY(我的模版)/PUBLIC(公开模版)，不传默认 MY
- --limit <Int>: 返回数量上限
- --cursor <String>: 分页游标

## Related
- dws doc template apply
- dws doc template search
