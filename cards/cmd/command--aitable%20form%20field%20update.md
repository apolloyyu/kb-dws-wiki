# dws aitable form field update

kind: command
completeness: full
usage: dws aitable form field update
description: 更新表单字段
example: dws aitable form field update --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --field-id FIELD_ID --required true
source: internal/helpers/aitable.go:5518
visible_flags: 6

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --field-id <String>: 目标字段 ID（通过 form field list 获取）(必填)
- --required <String>: 设置字段在表单中的必填状态 (true/false)
- --field-description <String>: 设置字段在表单中的描述文案

## Related
- dws aitable form field hide
- dws aitable form field list
