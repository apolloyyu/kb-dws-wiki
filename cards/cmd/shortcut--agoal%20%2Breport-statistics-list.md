# dws agoal +report-statistics-list

kind: shortcut
completeness: full
usage: dws agoal +report-statistics-list
description: 查询周月报规则提交统计
source: internal/shortcut/agoal/agoal.go:156
visible_flags: 1

## Flags
- --keyword <String>: 规则名称关键词；传入保证不匹配的关键词可得到合法空集合

## Related
- dws agoal +contract-fields
- dws agoal +obj-template-list
- dws agoal +report-submit-detail
- dws agoal +user-rules
