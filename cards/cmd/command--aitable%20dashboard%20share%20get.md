# dws aitable dashboard share get

kind: command
completeness: full
usage: dws aitable dashboard share get
description: Retrieve the current public-sharing configuration of a dashboard.
example: dws aitable dashboard share get --base-id BASE_ID --dashboard-id DASHBOARD_ID
use_when: When the agent needs to verify whether a dashboard has an active external share link.
source: internal/helpers/aitable.go:6451
visible_flags: 2

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)

## Related
- dws aitable dashboard share update
