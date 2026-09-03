# dws agoal strategy list

kind: command
completeness: full
usage: dws agoal strategy list
description: 获取战略解码列表
example: dws agoal strategy list --scope-type PERSONAL --scope-id USER_ID
source: internal/helpers/agoal.go:48
visible_flags: 3

## Flags
- --scope-type <String>: 解码范围类型: DEPT/PERSONAL (必填)
- --scope-id <String>: scope-type 对应的钉钉部门 id 或用户 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal strategy detail
- dws agoal strategy update
