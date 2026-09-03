# dws attendance +get-self-setting

kind: shortcut
completeness: full
description: 查询个人规则设置（打卡提醒/极速打卡/缺卡提醒等）
source: internal/shortcut/attendance/attendance.go:1654
visible_flags: 2

## Flags
- --setting-scene <String>: —
- --user <String>: --user 不能为空，表示查询用户 userId

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
