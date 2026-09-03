# dws agoal user rules

kind: command
completeness: full
description: 获取用户的规则周期列表
source: internal/helpers/agoal.go:399
visible_flags: 2

## Flags
- --user-id <String>: 要查询的人员钉钉 id (可选，默认取操作人)
- --request-id <String>: requestId (可选)

## Related
- dws agoal user objectives
