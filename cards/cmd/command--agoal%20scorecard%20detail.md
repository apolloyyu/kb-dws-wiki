# dws agoal scorecard detail

kind: command
completeness: full
usage: dws agoal scorecard detail
description: 获取计分卡详情
example: dws agoal scorecard detail --selected-time "2026-01-01T00:00:00+08:00" --dept-id DEPT_ID
source: internal/helpers/agoal.go:263
visible_flags: 3

## Flags
- --selected-time <String>: ISO-8601 时间字符串，如 \"2026-01-01T00:00:00+08:00\" (必填)
- --dept-id <String>: 部门 id (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal scorecard entity-detail
- dws agoal scorecard search-entities
- dws agoal scorecard update
