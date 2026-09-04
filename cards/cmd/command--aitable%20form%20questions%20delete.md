# dws aitable form questions delete

kind: command
completeness: full
usage: dws aitable form questions delete
description: 从表单删除题目（等价于 field delete，不可逆）
example: dws aitable form questions delete --base-id BASE_ID --table-id TABLE_ID --field-id fldXXX --yes
source: internal/helpers/aitable.go:5446
visible_flags: 3

## Flags
- --base-id <String>: Base ID（通过 base list 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --field-id <String>: 待删除字段 ID（通过 table get 获取）(必填)

## Related
- dws aitable form questions create
