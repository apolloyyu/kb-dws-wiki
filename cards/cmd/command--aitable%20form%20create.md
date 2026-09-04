# dws aitable form create

kind: command
completeness: full
usage: dws aitable form create
description: 创建表单视图
example: dws aitable form create --base-id BASE_ID --table-id TABLE_ID --name "员工信息收集"
source: internal/helpers/aitable.go:5202
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --name <String>: 新表单名称 (必填)
- --description <String>: 表单描述（创建后可用 form update 调整）

## Related
- dws aitable form delete
- dws aitable form field
- dws aitable form get
- dws aitable form list
- dws aitable form questions
- dws aitable form share
