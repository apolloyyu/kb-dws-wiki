# dws aitable view update filter

kind: command
completeness: full
usage: dws aitable view update filter
description: 更新视图 filter 配置
example: dws aitable view update filter --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --json '[{"operator":"and","operands":[{"operator":"date_eq","operands":["fldDate",{"type":"relative","period":"month","offset":0}]}]}]'
source: internal/helpers/aitable.go:5378
visible_flags: 1

## Flags
- --json <String>: filter 数组 JSON；实体值使用结构化稳定身份或 entityName，日期保留 operator 专用 offset/timestamp JSON 类型 (必填)

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update frozen-cols
- dws aitable view update group
