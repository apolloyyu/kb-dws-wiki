# dws attendance +search-adjustment-rule

kind: shortcut
completeness: full
usage: dws attendance +search-adjustment-rule
description: 查询当前用户可管理的补卡规则列表
source: internal/shortcut/attendance/attendance.go:1018
visible_flags: 3

## Flags
- --query <String>: 补卡规则名称关键字，模糊搜索
- --page <Int>: —
- --limit <Int>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
