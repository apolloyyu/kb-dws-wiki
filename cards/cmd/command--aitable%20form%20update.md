# dws aitable form update

kind: command
completeness: full
usage: dws aitable form update
description: 更新表单配置
example: dws aitable form update --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --title "员工信息收集"
source: internal/helpers/aitable.go:5341
visible_flags: 6

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标表单视图 ID (必填)
- --title <String>: 表单标题（与 --name 等价，二选一）
- --name <String>: 表单标题（与 --title 等价）
- --description <String>: 表单描述

## Related
- dws aitable form create
- dws aitable form delete
- dws aitable form field
- dws aitable form get
- dws aitable form list
- dws aitable form questions
