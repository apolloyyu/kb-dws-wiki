# dws aitable field update

kind: command
completeness: full
usage: dws aitable field update
description: Update a field's name, type, or options in a datasheet.
example: dws aitable field update --base-id BASE_ID --table-id TABLE_ID --field-id FIELD_ID --name "新字段名"
use_when: When the agent needs to rename a column or change its type/options without recreating it.
source: internal/helpers/aitable.go:2487
visible_flags: 6

## Flags
- --base-id <String>: Base ID（可通过 base list 获取）(必填)
- --table-id <String>: Table ID（可通过 base get 获取）(必填)
- --field-id <String>: Field ID（可通过 table get 获取）(必填)
- --name <String>: 更新后的字段名称，最大100字。不修改名称时省略
- --config <String>: 更新后的字段配置 JSON，结构与 field create 的 config 完全一致。不修改配置时省略。更新 singleSelect/multipleSelect 的 options 时需传入完整列表，系统以新列表整体覆盖；已有选项应回传原 id，新增选项无需传 id
- --ai-config <String>: 更新后的 AI 配置 JSON，不修改 AI 配置时省略（与 MCP update_field.aiConfig 对齐）

## Related
- dws aitable field create
- dws aitable field delete
- dws aitable field get
- dws aitable field list
- dws aitable field search-options
