# dws attendance vacation balance

kind: command
completeness: full
description: 查询指定员工假期余额
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
