# dws agoal scorecard update

kind: command
completeness: full
description: 更新战略解码
source: internal/helpers/agoal.go:98
visible_flags: 3

## Flags
- --profile-id <String>: 战略解码 id (必填)
- --content <String>: 实体列表 JSON 数组 (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal scorecard detail
- dws agoal scorecard entity-detail
