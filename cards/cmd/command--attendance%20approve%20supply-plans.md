# dws attendance approve supply-plans

kind: command
completeness: full
usage: dws attendance approve supply-plans
description: 匹配补卡目标异常班次（服务端口径，与客户端发起页一致）
example: dws attendance approve supply-plans --time "2026-08-05 04:00"
source: internal/helpers/attendance.go:1284
visible_flags: 2

## Flags
- --time <String>: 补卡时间点 yyyy-MM-dd HH:mm（对齐补卡模板 DDDateField 子控件 format）(必填)
- --user <String>: 补卡人 userId（代他人提交时必填；缺省为当前登录用户）

## Related
- dws attendance approve leave-check
- dws attendance approve leave-duration
- dws attendance approve leave-types
- dws attendance approve list
- dws attendance approve supply-check
- dws attendance approve templates
