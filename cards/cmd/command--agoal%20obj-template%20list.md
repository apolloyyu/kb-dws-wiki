# dws agoal obj-template list

kind: command
completeness: full
description: 获取战略解码列表
source: internal/helpers/agoal.go:48
visible_flags: 3

## Flags
- --scope-type <String>: 解码范围类型: DEPT/PERSONAL (必填)
- --scope-id <String>: scope-type 对应的钉钉部门 id 或用户 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal obj-template create-or-update
