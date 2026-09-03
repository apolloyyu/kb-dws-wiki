# dws attendance +get-group-filtered

kind: shortcut
completeness: full
description: 按需查询考勤组成员/打卡地址/蓝牙/Wifi 子集
source: internal/shortcut/attendance/attendance.go:1413
visible_flags: 5

## Flags
- --group-id <Int>: 考勤组 ID
- --member <Bool>: 是否查询考勤组成员信息
- --position <Bool>: 是否查询打卡地址
- --wifi <Bool>: 是否查询打卡 Wifi
- --bles <Bool>: 是否查询打卡蓝牙

## Related
- dws attendance +boss-check
- dws attendance +check-record
- dws attendance +check-result
- dws attendance +create-class
- dws attendance +create-group
- dws attendance +get-adjustment-rule
