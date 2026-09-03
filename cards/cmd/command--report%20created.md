# dws report created

kind: command
completeness: full
usage: dws report created
description: [deprecated] 已废弃，请改用 `dws report outbox list`
example: dws report created --cursor 0 --size 20
source: internal/helpers/report.go:507
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
- dws report detail
- dws report entry
- dws report inbox
- dws report list
- dws report outbox
