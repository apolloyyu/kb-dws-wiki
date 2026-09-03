# dws aitable field delete

kind: command
completeness: full
usage: dws aitable field delete
description: Delete a field from a datasheet by field ID; all values in that column are removed.
example: dws aitable field delete --base-id BASE_ID --table-id TABLE_ID --field-id FIELD_ID --yes
use_when: When the agent is cleaning up unused or deprecated columns in a datasheet.
source: internal/helpers/aitable.go:2617
visible_flags: 3

## Flags
- --base-id <String>: Base ID（通过 base list 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --field-id <String>: 待删除字段 ID（通过 table get 获取）(必填)

## Related
- dws aitable field create
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
