# dws report +template-search

kind: shortcut
completeness: full
usage: dws report +template-search
description: 按名称搜索可用日志模板
source: internal/shortcut/report/report.go:242
visible_flags: 1

## Flags
- --query <String>: 模板名称关键词，不区分大小写；--query 不能为空

## Related
- dws report +inbox-list
- dws report +outbox-list
- dws report +report-latest
