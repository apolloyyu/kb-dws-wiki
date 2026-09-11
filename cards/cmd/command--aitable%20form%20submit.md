# dws aitable form submit

kind: command
completeness: full
usage: dws aitable form submit
description: 提交已分享表单
example: dws aitable form submit --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --value '{"fldName":"张三"}'
source: internal/helpers/aitable.go:6775
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 已开启分享的表单视图 ID (必填)
- --value <String>: 表单值 JSON 对象字符串，key 必须为 fieldId (必填)

## Related
- dws aitable form create
- dws aitable form delete
- dws aitable form field
- dws aitable form get
- dws aitable form list
- dws aitable form questions
