# dws aitable dashboard get

kind: command
completeness: full
usage: dws aitable dashboard get
description: Retrieve a dashboard's layout, widget list, and metadata.
example: dws aitable dashboard get --base-id BASE_ID --dashboard-id DASHBOARD_ID
use_when: When the agent needs to inspect a dashboard before updating it or cloning it.
source: internal/helpers/aitable.go:6199
visible_flags: 2

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID（通过 base get 获取）(必填)

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard delete
- dws aitable dashboard share
- dws aitable dashboard update
