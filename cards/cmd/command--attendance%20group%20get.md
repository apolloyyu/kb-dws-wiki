# dws attendance group get

kind: command
completeness: full
usage: dws attendance group get
description: 根据考勤组 ID 查询考勤组全量信息
example: dws attendance group get --group-id 123456
source: internal/helpers/attendance.go:2214
visible_flags: 1

## Flags
- --group-id <Int64>: 考勤组 ID（必填）

## Related
- dws attendance group create
- dws attendance group filtered-get
- dws attendance group search
- dws attendance group update
- dws attendance group update-members
