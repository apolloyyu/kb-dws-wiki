# dws attendance summary

kind: command
completeness: full
description: Retrieve an aggregated attendance summary for a single user (totals of late, early-leave, absence, overtime).
use_when: When the agent needs a quick attendance health check without pulling raw records.
source: internal/helpers/attendance.go:2887
visible_flags: 3

## Flags
- --user <String>: 钉钉用户 ID（必填）
- --date <String>: 查询日期，格式 YYYY-MM-DD 或 YYYY-MM-DD HH:mm:ss（必填）
- --stats-type <String>: 统计类型：week（周统计）/ month（月统计）（必填）

## Related
- dws attendance boss-check
- dws attendance rules
