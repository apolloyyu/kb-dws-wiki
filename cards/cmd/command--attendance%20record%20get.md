# dws attendance record get

kind: command
completeness: full
usage: dws attendance record get
description: Query a user's detailed clock-in/clock-out attendance records for a given time range.
example: dws attendance record get --user USER_ID --date 2026-03-08
use_when: When the agent needs to verify punctuality, pull attendance evidence, or build an attendance report for an individual.
source: internal/helpers/attendance.go:589
visible_flags: 2

## Flags
- --user <String>: 钉钉用户 ID (必填)
- --date <String>: 查询日期，格式 YYYY-MM-DD (必填)

## Related
- none
