# dws aitable record group-stats

kind: command
completeness: full
usage: dws aitable record group-stats
description: 分组、去重及高级聚合统计
example: dws aitable record group-stats --base-id BASE_ID --table-id TABLE_ID --group '[{"fieldId":"fldCategory","direction":"ASC","fieldConfig":null,"arraySplitMode":true}]' --stats '[{"fieldId":"fldAmount","statsType":"sum"}]'
source: internal/helpers/aitable.go:2903
visible_flags: 8

## Flags
- --base-id <String>: Base ID（通过 base get 确认目标）(必填)
- --table-id <String>: Table ID（通过 table get 获取）(必填)
- --stats <String>: sum
- --filters <String>: 结构化过滤条件 JSON 对象；数值比较值必须是 JSON 数字
- --group <String>: —
- --sort <String>: 统计结果排序 DSL（JSON 数组字符串），映射到 MCP sortDsl
- --limit <Int>: 返回的分组结果数，范围 1-1000；省略表示不额外限制
- --data-version <String>: 可选数据版本；通常省略以使用最新版本

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record history-list
- dws aitable record list
