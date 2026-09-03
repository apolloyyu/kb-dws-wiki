# dws aitable view update field-widths

kind: command
completeness: full
usage: dws aitable view update field-widths
description: 更新视图字段列宽（仅 Grid）
example: dws aitable view update field-widths --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --field-id fldX --width 200
source: internal/helpers/aitable.go:4400
visible_flags: 3

## Flags
- --field-id <String>: 单字段 ID（配合 --width）
- --width <Int>: 字段列宽（配合 --field-id）
- --json <String>: 完整 fieldWidths map JSON

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
- dws aitable view update group
