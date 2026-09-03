# dws sheet template list

kind: command
completeness: full
usage: dws sheet template list
description: 获取表格模板列表
example: dws sheet template list
source: internal/helpers/sheet_template.go:18
visible_flags: 3

## Flags
- --source <String>: 模板来源: MY(我的模版)/PUBLIC(公开模版)，不传默认 MY
- --limit <Int>: 返回数量上限
- --cursor <String>: 分页游标

## Related
- dws sheet template apply
- dws sheet template search
