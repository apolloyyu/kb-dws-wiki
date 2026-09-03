# dws report sent

kind: command
completeness: full
usage: dws report sent
description: List reports the current user has created and sent out.
example: dws report sent --cursor 0 --size 20
use_when: When the agent reviews the user's own reporting history.
source: internal/helpers/report.go:499
visible_flags: 7

## Flags
- --cursor <Int>: 分页游标，首次传 0 (默认 0)
- --size <Int>: 每页条数，最大 20 (默认 20)
- --start <String>: 创建开始时间 ISO-8601 (默认最近 20 天；服务端单次查询跨度上限 20 天)
- --end <String>: 创建结束时间 ISO-8601 (默认最近 20 天；服务端单次查询跨度上限 20 天)
- --modified-start <String>: 修改开始时间 ISO-8601 (可选)
- --modified-end <String>: 修改结束时间 ISO-8601 (可选)
- --template-name <String>: 日志模板名称 (可选，不传查全部)

## Related
- dws report create
- dws report created
- dws report detail
- dws report entry
- dws report inbox
- dws report list
