# dws aitable table update

kind: command
completeness: full
usage: dws aitable table update
description: Update a datasheet's name or other metadata.
example: dws aitable table update --base-id BASE_ID --table-id TABLE_ID --name "新表名"
use_when: When the agent needs to rename a datasheet without altering its contents.
source: internal/helpers/aitable.go:2199
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID（用于定位目标表）(必填)
- --table-id <String>: 目标 Table ID（通过 base get 获取）(必填)
- --name <String>: 新表名。不能包含 / \\ ? * [ ] : 等特殊字符；与 --description / --record-name-key 三选一
- --description <String>: 更新后的数据表备注说明；与 --name / --record-name-key 三选一
- --record-name-key <String>: 行命名规则枚举键（如 task / project / event / customer 等固定枚举值）；与 --name / --description 三选一

## Related
- dws aitable table create
- dws aitable table delete
- dws aitable table get
- dws aitable table list
