# dws attendance +create-group

kind: shortcut
completeness: full
description: 创建考勤组（复杂子对象用 --group-vo JSON 传入）
source: internal/shortcut/attendance/attendance.go:1490
visible_flags: 4

## Flags
- --name <String>: 考勤组名称
- --type <String>: —
- --owner <String>: 考勤组主负责人 userId
- --group-vo <String>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +get-adjustment-rule
- dws attendance +get-approve-template
