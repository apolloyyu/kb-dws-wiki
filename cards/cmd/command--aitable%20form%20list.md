# dws aitable form list

kind: command
completeness: full
usage: dws aitable form list
description: 列出表单视图
example: dws aitable form list --base-id BASE_ID --table-id TABLE_ID
source: internal/helpers/aitable.go:5162
visible_flags: 2

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)

## Related
- dws aitable form create
- dws aitable form delete
- dws aitable form field
- dws aitable form get
- dws aitable form questions
- dws aitable form share
