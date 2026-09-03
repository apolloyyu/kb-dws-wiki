# dws attendance approve supply-check

kind: command
completeness: full
description: 提交前校验补卡资格（期限 / 次数 / 状态）
source: internal/helpers/attendance.go:1355
visible_flags: 2

## Flags
- --timestamp <Int64>: 选定班次的补卡时刻（毫秒时间戳，取自 supply-plans 输出的 supplyDate）(必填)
- --user <String>: 补卡人 userId（代他人提交时必填；缺省为当前登录用户）

## Related
- dws attendance approve leave-check
- dws attendance approve leave-duration
- dws attendance approve leave-types
- dws attendance approve list
- dws attendance approve supply-plans
- dws attendance approve templates
