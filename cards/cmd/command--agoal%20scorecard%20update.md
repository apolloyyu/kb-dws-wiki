# dws agoal scorecard update

kind: command
completeness: full
usage: dws agoal scorecard update
description: 更新计分卡
example: dws agoal scorecard update --dept-id DEPT_ID --selected-time "2025-01-01T00:00:00+08:00" --id SC_ID --tracking-period-type MONTHLY --content '[{"id":"dim1","title":"业绩","items":[{"id":"item1","title":"收入","target":"100"}]}]'
source: internal/helpers/agoal.go:316
visible_flags: 6

## Flags
- --dept-id <String>: 部门 id (必填)
- --selected-time <String>: ISO-8601 时间字符串，如 \"2026-01-01T00:00:00+08:00\" (必填)
- --id <String>: 计分卡 id (必填)
- --tracking-period-type <String>: 跟踪周期类型: MONTHLY/月度追踪、QUARTERLY/季度追踪 (必填)
- --content <String>: 内容 JSON 数组 (必填)
- --request-id <String>: requestId (可选)

## Related
- dws agoal scorecard detail
- dws agoal scorecard entity-detail
- dws agoal scorecard search-entities
