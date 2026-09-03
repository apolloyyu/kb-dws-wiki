# dws aitable view update fill-color-rule

kind: command
completeness: full
usage: dws aitable view update fill-color-rule
description: 更新视图数据高亮规则
example: dws aitable view update fill-color-rule --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --json '[]'
source: internal/helpers/aitable.go:4973
visible_flags: 1

## Flags
- --json <String>: conditionalFormats JSON 数组（整组替换；传 [] 清空）(必填)

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update filter
- dws aitable view update frozen-cols
- dws aitable view update group
