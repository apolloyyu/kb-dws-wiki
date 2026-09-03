# dws attendance +search-group

kind: shortcut
completeness: full
usage: dws attendance +search-group
description: 查询当前用户可管理的考勤组列表
source: internal/shortcut/attendance/attendance.go:1280
visible_flags: 6

## Flags
- --query <String>: 考勤组名称关键字，模糊搜索
- --type <String>: —
- --query-position <Bool>: 是否查询地理定位和 Wifi 名称
- --query-ble <Bool>: 是否查询蓝牙设备列表
- --page <Int>: —
- --limit <Int>: —

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
