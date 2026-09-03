# dws attendance globalsetting get

kind: command
completeness: full
description: 查询个人考勤详情
source: internal/helpers/attendance.go:589
visible_flags: 2

## Flags
- --user <String>: 钉钉用户 ID (必填)
- --date <String>: 查询日期，格式 YYYY-MM-DD (必填)

## Related
- dws attendance globalsetting save
