# dws attendance selfsetting save

kind: command
completeness: partial
usage: dws attendance selfsetting save
description: 更新保存个人规则设置
example: dws attendance selfsetting save --setting-scene checkResultNotify --user CURRENT_USER_ID --check-result-msg 1
source: internal/helpers/attendance.go:3167
visible_flags: 3
partial_reason: unverified_flags,empty_flag_name

## Flags
- --setting-scene <String>: 更新设置项：checkRemind/fastCheck/checkResultNotify/lackRemind/personalAttendStatNotify/bossAttendStatNotify（必填）
- --user <String>: 当前登录用户本人的 userId（必填；不支持更新其他员工）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance selfsetting get
