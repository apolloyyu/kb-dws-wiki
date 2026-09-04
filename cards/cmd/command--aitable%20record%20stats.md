# dws aitable record stats

kind: command
completeness: full
usage: dws aitable record stats
description: 整表或过滤后的字段聚合统计
example: dws aitable record stats --base-id BASE_ID --table-id TABLE_ID --stats '[{"fieldId":"fldAmount","statsType":"SUM"}]'
source: internal/helpers/aitable.go:2816
visible_flags: 9

## Flags
- --base-id <String>: Base ID（通过 base get 确认目标）(必填)
- --table-id <String>: Table ID（通过 table get 获取）(必填)
- --stats <String>: SUM
- --filters <String>: 结构化过滤条件 JSON 对象；数值比较值必须是 JSON 数字
- --sort <String>: ASC
- --limit <Int>: 参与统计的最大记录数；省略表示统计全部匹配记录
- --keyword <String>: 全文关键词，仅匹配的记录参与统计
- --search-field-ids <String>: 关键词搜索字段 ID 列表，逗号分隔；仅 --keyword 非空时生效
- --data-version <String>: 可选数据版本；通常省略以使用最新版本

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record get
- dws aitable record group-stats
- dws aitable record history-list
