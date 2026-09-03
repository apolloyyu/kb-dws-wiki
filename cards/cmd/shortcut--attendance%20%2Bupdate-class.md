# dws attendance +update-class

kind: shortcut
completeness: full
description: 更新已有班次（仅传要修改的字段）
source: internal/shortcut/attendance/attendance.go:936
visible_flags: 4

## Flags
- --class-id <Int>: 班次 ID
- --name <String>: 班次名称（不传则保持原值）
- --owner <String>: 班次负责人 userId（不传则保持原值）
- --class-vo <String>: 完整 TopAtClassVO JSON（checkTime 用 HH:mm，自动转时间戳）

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
