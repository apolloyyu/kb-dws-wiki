# dws agoal contract list

kind: command
completeness: full
usage: dws agoal contract list
description: 获取经营合约列表
example: dws agoal contract list --scope-type PERSONAL --scope-id USER_ID
source: internal/helpers/agoal.go:144
visible_flags: 3

## Flags
- --scope-type <String>: 合约范围类型: DEPT/PERSONAL (必填)
- --scope-id <String>: scope-type 对应的钉钉部门 id 或用户 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal contract detail
- dws agoal contract fields
- dws agoal contract update
