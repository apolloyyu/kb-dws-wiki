# dws attendance +update-leave-type

kind: shortcut
completeness: full
description: 更新已有假期规则（仅传要修改的字段）
source: internal/shortcut/attendance/attendance.go:2065
visible_flags: 7

## Flags
- --leave-code <String>: 假期编码
- --name <String>: 假期名称
- --unit <String>: —
- --paid <Bool>: 是否带薪假期
- --per-hours <Int>: 一天折算小时数
- --when-can-leave <String>: —
- --visibility-rules <String>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
