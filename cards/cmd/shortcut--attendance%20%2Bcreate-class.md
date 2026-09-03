# dws attendance +create-class

kind: shortcut
completeness: full
usage: dws attendance +create-class
description: 创建班次（checkTime 用 HH:mm，自动转时间戳）
source: internal/shortcut/attendance/attendance.go:896
visible_flags: 3

## Flags
- --name <String>: 班次名称
- --owner <String>: 班次负责人 userId
- --class-vo <String>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-group
- dws attendance +get-adjustment-rule
- dws attendance +get-approve-template
