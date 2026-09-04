# dws aitable form field hide

kind: command
completeness: full
usage: dws aitable form field hide
description: 切换表单字段隐藏
example: dws aitable form field hide --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --field-id FIELD_ID --hidden true
source: internal/helpers/aitable.go:5569
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --field-id <String>: 目标字段 ID (必填)
- --hidden <String>: true 隐藏字段，false 显示字段

## Related
- dws aitable form field list
- dws aitable form field update
