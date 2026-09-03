# dws attendance vacation save-balance

kind: command
completeness: full
usage: dws attendance vacation save-balance
description: 设置员工假期余额
example: dws attendance vacation save-balance --target user001 --leave-code a1b2c3d4-e5f6-7890-abcd-ef1234567890 --num 8 --reason "年度发放"
source: internal/helpers/attendance.go:4076
visible_flags: 7

## Flags
- --target <String>: 目标员工工号（必填）
- --leave-code <String>: 假期编码（必填）
- --num <String>: 余额数量（必填）
- --reason <String>: 变更原因（必填）
- --start <String>: 有效期开始日期 YYYY-MM-DD
- --end <String>: 有效期结束日期 YYYY-MM-DD
- --user-say-yes <Bool>: 用户已确认，跳过交互式确认提示（Agent 调用时传 true 前必须完成用户二次确认）

## Related
- dws attendance vacation balance
- dws attendance vacation records
- dws attendance vacation types
- dws attendance vacation update-type
