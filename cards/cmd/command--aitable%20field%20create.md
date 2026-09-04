# dws aitable field create

kind: command
completeness: full
usage: dws aitable field create
description: Create one or more fields in a datasheet with specified types and options.
example: dws aitable field create --base-id BASE_ID --table-id TABLE_ID
use_when: When the agent is extending a datasheet's schema to capture new attributes.
source: internal/helpers/aitable.go:2376
visible_flags: 7

## Flags
- --base-id <String>: Base ID（通过 base list 获取）(必填)
- --table-id <String>: Table ID（通过 base get 获取）(必填)
- --fields <String>: 待新增字段列表 JSON 数组，至少包含 1 个字段，单次最多 15 个。系统会按数组顺序依次创建，返回结果顺序与入参保持一致，并逐项标明成功/失败状态。若是单个字段可直接使用 --name/--type/--config
- --name <String>: 要创建的单字段名称（与 --type 配合使用，替代 --fields）
- --type <String>: 要创建的单字段类型（需要配合 --name，参考 table create 的内置类型）
- --config <String>: 单字段的额外配置 JSON（如 options，配合 --name/--type 使用）
- --ai-config <String>: 单字段 AI 配置 JSON（如 outputType/prompt，配合 --name/--type 使用）

## Related
- dws aitable field delete
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
- dws aitable field update
