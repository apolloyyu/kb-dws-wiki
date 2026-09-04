# dws aitable table create

kind: command
completeness: full
usage: dws aitable table create
description: Create a new datasheet (table) inside a Base.
example: dws aitable table create --base-id BASE_ID --name "任务表"
use_when: When the agent needs another table alongside existing ones in the same Base.
source: internal/helpers/aitable.go:2097
visible_flags: 3

## Flags
- --base-id <String>: 目标 Base ID（通过 base list 获取）(必填)
- --name <String>: 表格名称，1~100 个字符；不能包含 / \\ ? * [ ] : 等字符 (必填)
- --fields <String>: 建表时随附创建的初始字段 JSON 数组，至少 1 个，单次最多 15 个。若传空数组 []，系统会自动补一个名为'标题'的 primaryDoc 首列

## Related
- dws aitable table delete
- dws aitable table get
- dws aitable table list
- dws aitable table update
