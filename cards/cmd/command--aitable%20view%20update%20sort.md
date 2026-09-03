# dws aitable view update sort

kind: command
completeness: full
usage: dws aitable view update sort
description: 更新视图 sort 配置
example: dws aitable view update sort --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --json '[{"fieldId":"fldX","direction":"asc"}]'
source: internal/helpers/aitable.go:4554
visible_flags: 1

## Flags
- --json <String>: sort 数组 JSON

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
