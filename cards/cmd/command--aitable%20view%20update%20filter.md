# dws aitable view update filter

kind: command
completeness: full
usage: dws aitable view update filter
description: 更新视图 filter 配置
example: dws aitable view update filter --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --json '[{"operator":"eq","operands":["fldX","value"]}]'
source: internal/helpers/aitable.go:4519
visible_flags: 1

## Flags
- --json <String>: filter 数组 JSON

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update frozen-cols
- dws aitable view update group
