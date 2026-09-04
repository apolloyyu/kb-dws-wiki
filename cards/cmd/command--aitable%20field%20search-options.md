# dws aitable field search-options

kind: command
completeness: full
usage: dws aitable field search-options
description: 搜索单选/多选字段的选项
example: dws aitable field search-options --base-id BASE_ID --table-id TABLE_ID --field-id FIELD_ID
source: internal/helpers/aitable.go:2572
visible_flags: 5

## Flags
- --base-id <String>: Base ID（通过 base list 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --field-id <String>: 目标字段 ID，必须是 singleSelect 或 multipleSelect 类型；通过 table get / field get 获取 (必填)
- --keyword <String>: 模糊搜索关键词，大小写不敏感，按 contains 匹配 option name；不传则返回全部 options
- --limit <Int>: 返回的最大 option 数量，默认 3000（全量返回），最大 3000；传入较小值可减少响应体积

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field get
- dws aitable field list
- dws aitable field update
