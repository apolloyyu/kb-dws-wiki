# dws attendance approve leave-duration

kind: command
completeness: full
usage: dws attendance approve leave-duration
description: 计算请假时长（服务端口径，与客户端发起页一致）
example: dws attendance approve leave-duration --leave-code <leaveCode> --start "2026-08-13 09:00" --end "2026-08-14 18:00"
source: internal/helpers/attendance.go:1097
visible_flags: 4

## Flags
- --leave-code <String>: 假期类型编码（form-schema 套件 options[i].leaveCode）(必填)
- --start <String>: 开始时间（格式随模板 unit：hour/halfHour/limitHour → yyyy-MM-dd HH:mm；day → yyyy-MM-dd；halfDay → yyyy-MM-dd 上午/下午）(必填)
- --end <String>: 结束时间（格式同 --start）(必填)
- --user <String>: 发起人 userId（代他人提交时必填；缺省为当前登录用户）

## Related
- dws attendance approve leave-check
- dws attendance approve leave-types
- dws attendance approve list
- dws attendance approve supply-check
- dws attendance approve supply-plans
- dws attendance approve templates
