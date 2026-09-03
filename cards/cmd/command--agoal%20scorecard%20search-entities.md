# dws agoal scorecard search-entities

kind: command
completeness: full
usage: dws agoal scorecard search-entities
description: 搜索计分卡指标与关键事项
example: dws agoal scorecard search-entities --keyword "业绩"
source: internal/helpers/agoal.go:363
visible_flags: 4

## Flags
- --keyword <String>: 搜索关键词，标题模糊匹配 (必填)
- --request-id <String>: requestId (可选)
- --page <Int>: 页码，默认 1 (可选)
- --page-size <Int>: 每页数量，最大 100 (可选)

## Related
- dws agoal scorecard detail
- dws agoal scorecard entity-detail
- dws agoal scorecard update
