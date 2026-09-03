# dws aitable view update

kind: command
completeness: full
usage: dws aitable view update
description: Update a view's name, filter, sort, grouping, or visible fields.
example: dws aitable view update --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --name "新视图名"
use_when: When the agent refines an existing view's configuration after inspection.
source: internal/helpers/aitable.go:4159
visible_flags: 6

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-id <String>: 目标 View ID (必填)
- --name <String>: 新的视图名称
- --desc <String>: 新的视图描述 JSON，不修改时省略；如需清空可传 {\"content\":[]}
- --config <String>: 视图配置更新项 JSON（含 visibleFieldIds、filter、sort、group、fieldWidths 等）

## Related
- dws aitable view create
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view lock
