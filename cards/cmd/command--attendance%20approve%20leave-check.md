# dws attendance approve leave-check

kind: command
completeness: full
description: 提交前校验请假资格（时间冲突 / 可撤销单 / 额度）
source: internal/helpers/attendance.go:1173
visible_flags: 8

## Flags
- --leave-code <String>: 假期类型编码 (必填)
- --process-code <String>: 审批模板 processCode (必填)
- --start <String>: 开始时间（对齐 PC 端校验接口传参：hour 原样 yyyy-MM-dd HH:mm；day 传 日期+ 00:00；halfDay 上午传 00:00、下午传 12:00）(必填)
- --end <String>: 结束时间（hour 原样；day 传 日期+ 23:59；halfDay 上午传 12:00、下午传 23:59）(必填)
- --duration-day <Float64>: 时长（天），取自 leave-duration 输出的 durationInDay (必填)
- --duration-hour <Float64>: 时长（小时），取自 leave-duration 输出的 durationInHour (必填)
- --user <String>: 发起人 userId（代他人提交时必填；缺省为当前登录用户）
- --proc-inst-id <String>: 修改已有实例场景的原实例 ID（新发起不传）

## Related
- dws attendance approve leave-duration
- dws attendance approve leave-types
- dws attendance approve list
- dws attendance approve supply-check
- dws attendance approve supply-plans
- dws attendance approve templates
