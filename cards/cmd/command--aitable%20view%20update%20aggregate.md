# dws aitable view update aggregate

kind: command
completeness: full
usage: dws aitable view update aggregate
description: 更新视图字段聚合统计（仅 Grid）
example: dws aitable view update aggregate --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --field-id fldX --action SUM
source: internal/helpers/aitable.go:4341
visible_flags: 4

## Flags
- --field-id <String>: 单字段 ID（配合 --action 写入单个聚合）
- --action <String>: 聚合 action: SUM|AVG|MAX|MIN|MEDIAN|RANGE|...（配合 --field-id）
- --clear-field-id <String>: 清除聚合的字段 ID 列表 (CSV)
- --json <String>: 完整 aggregate map JSON

## Related
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
- dws aitable view update group
