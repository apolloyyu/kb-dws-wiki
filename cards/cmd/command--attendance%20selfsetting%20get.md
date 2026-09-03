# dws attendance selfsetting get

kind: command
completeness: full
usage: dws attendance selfsetting get
description: 查询个人规则设置
example: dws attendance selfsetting get --setting-scene checkRemind --user CURRENT_USER_ID
source: internal/helpers/attendance.go:3033
visible_flags: 2

## Flags
- --setting-scene <String>: 查询设置项：checkRemind/fastCheck/checkResultNotify/lackRemind/personalAttendStatNotify/bossAttendStatNotify（必填）
- --user <String>: 当前登录用户本人的 userId（必填；不支持查询其他员工）

## Related
- dws attendance selfsetting save
