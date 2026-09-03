# dws attendance group filtered-get

kind: command
completeness: full
usage: dws attendance group filtered-get
description: 根据考勤组 ID 按需查询成员/打卡地址/蓝牙/Wifi 信息
example: dws attendance group filtered-get --group-id 123456 --member
source: internal/helpers/attendance.go:2263
visible_flags: 5

## Flags
- --group-id <Int64>: 考勤组 ID（必填）
- --member <Bool>: 是否查询考勤组成员信息（可选）
- --position <Bool>: 是否查询打卡地址（可选）
- --wifi <Bool>: 是否查询打卡 Wifi（可选）
- --bles <Bool>: 是否查询打卡蓝牙（可选）

## Related
- dws attendance group create
- dws attendance group get
- dws attendance group search
- dws attendance group update
- dws attendance group update-members
