# dws aitable view update name

kind: command
completeness: full
usage: dws aitable view update name
description: 重命名视图（= view update --name 的便捷子命令）
example: dws aitable view update name --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --name "新视图名"
source: internal/helpers/aitable.go:4636
visible_flags: 1

## Flags
- --name <String>: 新视图名称 (必填)

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
