# dws agoal scorecard entity-detail

kind: command
completeness: full
usage: dws agoal scorecard entity-detail
description: 获取计分卡实体详情
example: dws agoal scorecard entity-detail --sc-id SC_ID --entity-id ENTITY_ID
source: internal/helpers/agoal.go:293
visible_flags: 3

## Flags
- --sc-id <String>: 计分卡 id (必填)
- --entity-id <String>: 计分卡实体 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal scorecard detail
- dws agoal scorecard search-entities
- dws agoal scorecard update
