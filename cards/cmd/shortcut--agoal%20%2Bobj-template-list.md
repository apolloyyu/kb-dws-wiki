# dws agoal +obj-template-list

kind: shortcut
completeness: full
description: 分页查询 Agoal 目标模板
source: internal/shortcut/agoal/agoal.go:204
visible_flags: 3

## Flags
- --keyword <String>: 模板关键词；传入保证不匹配的关键词可得到合法空集合
- --page <Int>: —
- --page-size <Int>: —

## Related
- dws agoal +contract-fields
- dws agoal +report-statistics-list
- dws agoal +report-submit-detail
- dws agoal +user-rules
