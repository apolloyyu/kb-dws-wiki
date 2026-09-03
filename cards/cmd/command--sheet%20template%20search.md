# dws sheet template search

kind: command
completeness: full
description: 搜索表格模板
source: internal/helpers/sheet_template.go:71
visible_flags: 4

## Flags
- --query <String>: 搜索关键词 (必填)
- --source <String>: 模板来源: MY(我的模版)/PUBLIC(公开模版)，不传默认 MY
- --limit <Int>: 返回数量上限
- --cursor <String>: 分页游标

## Related
- dws sheet template apply
- dws sheet template list
