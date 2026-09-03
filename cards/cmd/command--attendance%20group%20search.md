# dws attendance group search

kind: command
completeness: full
usage: dws attendance group search
description: 查询当前用户可管理的考勤组列表
example: dws attendance group search --query "研发"
source: internal/helpers/attendance.go:2115
visible_flags: 6

## Flags
- --query <String>: 考勤组名称关键字，模糊搜索（可选）
- --type <String>: 考勤组类型：FIXED 固定班制 / TURN 排班制 / NONE 自由工时（可选）
- --query-position <Bool>: 是否查询地理定位和 Wifi 名称（可选）
- --query-ble <Bool>: 是否查询蓝牙设备列表（可选）
- --page <Int>: 页码，从 1 开始（默认 1，可选）
- --limit <Int>: 每页条数，200 以内（默认 20，可选）

## Related
- dws attendance group create
- dws attendance group filtered-get
- dws attendance group get
- dws attendance group update
- dws attendance group update-members
