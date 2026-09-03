# dws attendance approve templates

kind: command
completeness: full
description: 查询补卡/请假/加班/外出/出差审批提交链接
source: internal/helpers/attendance.go:962
visible_flags: 1

## Flags
- --type <String>: 审批类型：repair-check/patch/补卡、leave/请假、overtime/加班，或 REPAIR_CHECK/LEAVE/OVERTIME（必填）

## Related
- dws attendance approve leave-check
- dws attendance approve leave-duration
- dws attendance approve leave-types
- dws attendance approve list
- dws attendance approve supply-check
- dws attendance approve supply-plans
