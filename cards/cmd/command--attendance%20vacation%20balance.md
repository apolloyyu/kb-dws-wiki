# dws attendance vacation balance

kind: command
completeness: full
usage: dws attendance vacation balance
description: 查询指定员工假期余额
example: dws attendance vacation balance --users userId1,userId2 --leave-code a1b2c3d4-e5f6-7890-abcd-ef1234567890
source: internal/helpers/attendance.go:3735
visible_flags: 2

## Flags
- --users <String>: 目标员工 ID 列表，逗号分隔 (必填)
- --leave-code <String>: 假期规则 code (必填，服务端要求非空，不传返回 INVALID_PARAMS)

## Related
- dws attendance vacation records
- dws attendance vacation save-balance
- dws attendance vacation types
- dws attendance vacation update-type
