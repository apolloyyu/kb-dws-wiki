# dws agoal +report-submit-detail

kind: shortcut
completeness: full
usage: dws agoal +report-submit-detail
description: 分页查询周月报人员提交详情
source: internal/shortcut/agoal/agoal.go:394
visible_flags: 6

## Flags
- --template-id <String>: 周月报规则模板稳定 ID
- --submit-state <String>: 提交状态
- --query-date <String>: 可选 ISO-8601 日期或时间
- --keyword <String>: 可选人员名称关键词；可用于保证零命中
- --page <Int>: —
- --page-size <Int>: —

## Related
- dws agoal +contract-fields
- dws agoal +obj-template-list
- dws agoal +report-statistics-list
- dws agoal +user-rules
