# dws attendance globalsetting save

kind: command
completeness: full
usage: dws attendance globalsetting save
description: 更新保存全局规则设置（仅管理员）
example: dws attendance globalsetting save --scope 企业 --setting-scene checkRemind --check-remind-corp=true --yes
source: internal/helpers/attendance.go:3359
visible_flags: 3

## Flags
- --setting-scene <String>: 更新设置项：checkRemind/fastCheck/checkResultNotify/lackRemind/personalAttendStatNotify/bossAttendStatNotify（必填）
- --scope <String>: 全局范围确认，必须明确输入：企业/全公司/所有人（必填）
- --yes <Bool>: 跳过确认提示

## Related
- dws attendance globalsetting get
