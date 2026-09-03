# dws aitable dashboard update

kind: command
completeness: full
usage: dws aitable dashboard update
description: Update an existing dashboard's layout, widgets, or metadata.
example: dws aitable dashboard update --base-id BASE_ID --dashboard-id DASHBOARD_ID --name "新名称"
use_when: When the agent adds, removes, or rearranges charts on an existing dashboard.
source: internal/helpers/aitable.go:6290
visible_flags: 4

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)
- --config <String>: Dashboard 配置更新项 JSON。可选，若只需改名可以用 --name 代替
- --name <String>: 要修改的新看板名称（替代 --config 简化操作）

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard get
- dws aitable dashboard share
