# dws aitable view update frozen-cols

kind: command
completeness: full
usage: dws aitable view update frozen-cols
description: 更新视图冻结列数
example: dws aitable view update frozen-cols --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --count 1
source: internal/helpers/aitable.go:4806
visible_flags: 1

## Flags
- --count <Int>: 冻结列数（>=0；0 表示取消冻结）(必填)

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update group
