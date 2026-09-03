# dws attendance globalsetting get

kind: command
completeness: full
usage: dws attendance globalsetting get
description: 查询全局规则设置（仅管理员）
example: dws attendance globalsetting get --scope 企业 --setting-scene checkRemind
source: internal/helpers/attendance.go:3292
visible_flags: 2

## Flags
- --setting-scene <String>: 查询设置项：checkRemind/fastCheck/checkResultNotify/lackRemind/personalAttendStatNotify/bossAttendStatNotify（必填）
- --scope <String>: 全局范围确认，必须明确输入：企业/全公司/所有人（必填）

## Related
- dws attendance globalsetting save
