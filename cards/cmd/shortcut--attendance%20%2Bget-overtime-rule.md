# dws attendance +get-overtime-rule

kind: shortcut
completeness: full
description: 根据加班规则主键 ID 查询加班规则详情
source: internal/shortcut/attendance/attendance.go:1139
visible_flags: 1

## Flags
- --overtime-id <Int>: --overtime-id 必须大于 0，表示加班规则主键 ID

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
