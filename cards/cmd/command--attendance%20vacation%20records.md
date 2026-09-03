# dws attendance vacation records

kind: command
completeness: full
usage: dws attendance vacation records
description: 查询指定员工假期余额变更记录
example: dws attendance vacation records --user USER_ID --leave-code a1b2c3d4-e5f6-7890-abcd-ef1234567890 --start 2026-04-01 --end 2026-04-22
source: internal/helpers/attendance.go:3801
visible_flags: 4

## Flags
- --user <String>: 指定查询员工 ID (必填)
- --leave-code <String>: 假期规则 code (必填，服务端要求非空，不传返回 INVALID_PARAMS)
- --start <String>: 查询开始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 查询结束日期，格式 YYYY-MM-DD (必填)

## Related
- dws attendance vacation balance
- dws attendance vacation save-balance
- dws attendance vacation types
- dws attendance vacation update-type
