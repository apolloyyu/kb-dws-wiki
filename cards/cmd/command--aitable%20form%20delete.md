# dws aitable form delete

kind: command
completeness: full
usage: dws aitable form delete
description: 删除表单
example: dws aitable form delete --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --yes
source: internal/helpers/aitable.go:5309
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID（通过 form list 获取）(必填)

## Related
- dws aitable form create
- dws aitable form field
- dws aitable form get
- dws aitable form list
- dws aitable form questions
- dws aitable form share
