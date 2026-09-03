# dws attendance shift list

kind: command
completeness: full
description: Batch-query the assigned shifts for a set of employees over a date range.
use_when: When the agent needs to plan around team shifts or compile a shift-based roster.
source: internal/helpers/attendance.go:862
visible_flags: 4

## Flags
- --users <String>: 用户 ID 列表，逗号分隔 (必填)
- --types <String>: 审批类型，逗号分隔：overtime/trip/leave/patch (必填)
- --start <String>: 起始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 结束日期，格式 YYYY-MM-DD (必填)

## Related
- none
