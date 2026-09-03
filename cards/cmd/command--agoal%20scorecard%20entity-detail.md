# dws agoal scorecard entity-detail

kind: command
completeness: full
description: 获取计分卡实体详情
source: internal/helpers/agoal.go:293
visible_flags: 3

## Flags
- --sc-id <String>: 计分卡 id (必填)
- --entity-id <String>: 计分卡实体 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal scorecard detail
- dws agoal scorecard update
