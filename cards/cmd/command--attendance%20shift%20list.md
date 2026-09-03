# dws attendance shift list

kind: command
completeness: full
usage: dws attendance shift list
description: Batch-query the assigned shifts for a set of employees over a date range.
example: dws attendance shift list --users userId1,userId2 --start 2026-03-03 --end 2026-03-07
use_when: When the agent needs to plan around team shifts or compile a shift-based roster.
source: internal/helpers/attendance.go:1448
visible_flags: 3

## Flags
- --users <String>: 用户 ID 列表，逗号分隔，最多 50 个 (必填)
- --start <String>: 开始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 结束日期，格式 YYYY-MM-DD (必填)

## Related
- none
