# dws aitable dashboard delete

kind: command
completeness: full
usage: dws aitable dashboard delete
description: Delete a dashboard from a Base by dashboard ID.
example: dws aitable dashboard delete --base-id BASE_ID --dashboard-id DASHBOARD_ID --yes
use_when: When the agent is removing an outdated dashboard.
source: internal/helpers/aitable.go:6355
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)
- --reason <String>: 删除原因

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard create
- dws aitable dashboard get
- dws aitable dashboard share
- dws aitable dashboard update
