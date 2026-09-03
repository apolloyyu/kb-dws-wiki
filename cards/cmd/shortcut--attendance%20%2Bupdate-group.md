# dws attendance +update-group

kind: shortcut
completeness: full
description: 更新考勤组配置（仅修改需要变更的字段）
source: internal/shortcut/attendance/attendance.go:1536
visible_flags: 7

## Flags
- --group-id <Int>: 考勤组 ID
- --name <String>: 考勤组名称
- --type <String>: —
- --owner <String>: 考勤组主负责人 userId
- --enable-outside-check <String>: —
- --class-ids <String>: —
- --group-vo <String>: 完整 groupVO JSON，用于修改复杂子对象

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
