# dws aitable record group-stats

kind: command
completeness: full
usage: dws aitable record group-stats
description: 分组、去重及高级聚合统计
example: dws aitable record group-stats --base-id BASE_ID --table-id TABLE_ID --group '[{"fieldId":"fldCategory","direction":"ASC","fieldConfig":null,"arraySplitMode":true}]' --sort '[{"fieldId":"fldCategory","direction":"DESC"}]' --stats '[{"fieldId":"fldAmount","statsType":"SUM"}]'
source: internal/helpers/aitable.go:3527
visible_flags: 8

## Flags
- --base-id <String>: Base ID（通过 base get 确认目标）(必填)
- --table-id <String>: Table ID（通过 table get 获取）(必填)
- --stats <String>: SUM
- --filters <String>: 结构化过滤条件 JSON 对象；数值比较值必须是 JSON 数字
- --group <String>: —
- --sort <String>: 分组结果排序 DSL（JSON 数组字符串）；排序 fieldId 必须同时出现在 --group 中
- --limit <Int>: 返回的分组结果数，范围 1-1000；省略使用服务端默认上限 1000
- --data-version <String>: 可选数据版本；通常省略以使用最新版本

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record create-sub
- dws aitable record delete
- dws aitable record get
- dws aitable record history-list
