# dws attendance approve leave-types

kind: command
completeness: full
usage: dws attendance approve leave-types
description: 查询可用假期类型及余额
example: dws attendance approve leave-types
source: internal/helpers/attendance.go:1037
visible_flags: 1

## Flags
- --user <String>: 目标员工 userId；不传时查询当前用户（查询他人需具备权限）

## Related
- dws attendance approve leave-check
- dws attendance approve leave-duration
- dws attendance approve list
- dws attendance approve supply-check
- dws attendance approve supply-plans
- dws attendance approve templates
