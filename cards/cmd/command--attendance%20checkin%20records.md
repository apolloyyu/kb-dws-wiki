# dws attendance checkin records

kind: command
completeness: full
usage: dws attendance checkin records
description: 查询指定员工的签到记录
example: dws attendance checkin records --operator-corp-id dingXXXXXX --operator-staff-id op001 --staff-ids user001,user002 --start "2026-04-01 00:00:00" --end "2026-04-07 00:00:00"
source: internal/helpers/attendance.go:4719
visible_flags: 5

## Flags
- --operator-corp-id <String>: 操作者企业 ID（必填）
- --operator-staff-id <String>: 操作者员工 ID（必填）
- --staff-ids <String>: 目标员工 ID 列表, 逗号分隔（必填），最多100人
- --start <String>: 开始时间, 格式 yyyy-MM-dd HH:mm:ss（必填），开始到结束最多7天
- --end <String>: 结束时间, 格式 yyyy-MM-dd HH:mm:ss（必填），开始到结束最多7天

## Related
- none
