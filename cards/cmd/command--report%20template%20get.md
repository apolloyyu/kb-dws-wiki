# dws report template get

kind: command
completeness: full
usage: dws report template get
description: 读取单个日志模版的字段定义
example: dws report template get --name <templateName>
source: internal/helpers/report.go:135
visible_flags: 1

## Flags
- --name <String>: 模版名称 (必填)

## Related
- dws report template detail
- dws report template list
