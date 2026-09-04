# dws aitable form get

kind: command
completeness: full
usage: dws aitable form get
description: 获取单个表单视图详情
example: dws aitable form get --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID
source: internal/helpers/aitable.go:5247
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)

## Related
- dws aitable form create
- dws aitable form delete
- dws aitable form field
- dws aitable form list
- dws aitable form questions
- dws aitable form share
