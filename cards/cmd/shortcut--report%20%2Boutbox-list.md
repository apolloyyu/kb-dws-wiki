# dws report +outbox-list

kind: shortcut
completeness: full
description: 列出我发出的日志
source: internal/shortcut/report/report.go:144
visible_flags: 7

## Flags
- --cursor <Int>: —
- --size <Int>: —
- --start <String>: 创建开始时间 ISO-8601；创建时间范围必须有效且不得超过 20 天
- --end <String>: 创建结束时间 ISO-8601；创建时间范围必须有效且不得超过 20 天
- --modified-start <String>: 修改开始时间 ISO-8601；修改时间必须成对提供、范围有效且不得超过 20 天
- --modified-end <String>: 修改结束时间 ISO-8601；修改时间必须成对提供、范围有效且不得超过 20 天
- --template-name <String>: 日志模板名称

## Related
- dws report +inbox-list
- dws report +report-latest
- dws report +template-search
