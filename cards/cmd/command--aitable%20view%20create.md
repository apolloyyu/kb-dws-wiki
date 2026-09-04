# dws aitable view create

kind: command
completeness: full
usage: dws aitable view create
description: Create a new view (grid, gallery, kanban, etc.) on a datasheet.
example: dws aitable view create --base-id BASE_ID --table-id TABLE_ID --view-type Grid
use_when: When the agent needs an alternate filtered/sorted presentation of the same datasheet data.
source: internal/helpers/aitable.go:4106
visible_flags: 7

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --table-id <String>: 所属 Table ID (必填)
- --view-type <String>: 视图类型：Grid、FormDesigner、Gantt、Calendar、Kanban、Gallery (必填)
- --view-sub-type <String>: 视图子类型，可选
- --name <String>: 视图名称，未传时自动生成
- --desc <String>: 视图描述 JSON，如 {\"content\":[]}
- --config <String>: 视图配置 JSON（含 visibleFieldIds、filter、sort、group 等）

## Related
- dws aitable view delete
- dws aitable view duplicate
- dws aitable view get
- dws aitable view list
- dws aitable view lock
- dws aitable view update
