# dws report +report-latest

kind: shortcut
completeness: full
description: 读取我最近提交的一篇日志详情
source: internal/shortcut/report/latest.go:26
visible_flags: 3

## Flags
- --keyword <String>: 按日志模板名称精确过滤
- --start <String>: 创建开始时间 ISO-8601；--start 与 --end 必须同时提供，且创建时间范围必须有效并不得超过 20 天
- --end <String>: 创建结束时间 ISO-8601；--start 与 --end 必须同时提供，且创建时间范围必须有效并不得超过 20 天

## Related
- dws report +inbox-list
- dws report +outbox-list
- dws report +template-search
