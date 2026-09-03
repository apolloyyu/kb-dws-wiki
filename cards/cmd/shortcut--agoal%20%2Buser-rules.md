# dws agoal +user-rules

kind: shortcut
completeness: full
description: 查询用户 Agoal 规则周期
source: internal/shortcut/agoal/agoal.go:331
visible_flags: 2

## Flags
- --user-id <String>: 可选用户稳定 ID；省略时查询本人
- --rule-id <String>: 可选稳定 ruleId；Shortcut 在严格验证完整数组后做精确等值筛选

## Related
- dws agoal +contract-fields
- dws agoal +obj-template-list
- dws agoal +report-statistics-list
- dws agoal +report-submit-detail
