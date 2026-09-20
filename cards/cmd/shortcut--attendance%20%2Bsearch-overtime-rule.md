# dws attendance +search-overtime-rule

kind: shortcut
completeness: full
usage: dws attendance +search-overtime-rule
description: 查询当前用户可管理的加班规则列表
source: internal/shortcut/attendance/attendance.go:1707
visible_flags: 3

## Flags
- --query <String>: 加班规则名称关键字，模糊搜索
- --page <Int>: —
- --limit <Int>: —

## Related
- dws attendance +boss-check
- dws attendance +calculate-approve-duration
- dws attendance +check-companion-schedules
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
