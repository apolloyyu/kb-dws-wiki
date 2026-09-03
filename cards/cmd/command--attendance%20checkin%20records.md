# dws attendance checkin records

kind: command
completeness: full
description: 查询指定员工假期余额变更记录
source: internal/helpers/attendance.go:3801
visible_flags: 4

## Flags
- --user <String>: 指定查询员工 ID (必填)
- --leave-code <String>: 假期规则 code (必填，服务端要求非空，不传返回 INVALID_PARAMS)
- --start <String>: 查询开始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 查询结束日期，格式 YYYY-MM-DD (必填)

## Related
- none
