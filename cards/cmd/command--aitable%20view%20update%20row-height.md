# dws aitable view update row-height

kind: command
completeness: full
usage: dws aitable view update row-height
description: 更新视图行高（单元格高度）
example: dws aitable view update row-height --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --cell-height 32
source: internal/helpers/aitable.go:4890
visible_flags: 1

## Flags
- --cell-height <Int>: 单元格高度（像素），合法档位 32 / 56 / 88 / 128 (必填)

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
