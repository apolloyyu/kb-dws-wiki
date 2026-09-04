# dws aitable view update visible-fields

kind: command
completeness: full
usage: dws aitable view update visible-fields
description: 更新视图可见字段列表
example: dws aitable view update visible-fields --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --field-ids fld1,fld2,fld3
source: internal/helpers/aitable.go:4464
visible_flags: 2

## Flags
- --field-ids <String>: 可见字段 ID 列表 (CSV)，整组替换原有顺序
- --json <String>: 可见字段 ID 数组 JSON

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
