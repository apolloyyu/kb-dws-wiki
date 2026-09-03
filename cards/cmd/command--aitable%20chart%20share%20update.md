# dws aitable chart share update

kind: command
completeness: full
usage: dws aitable chart share update
description: Enable, disable, or update the public-sharing configuration of a chart.
example: dws aitable chart share update --base-id BASE_ID --dashboard-id DASHBOARD_ID --chart-id CHART_ID --enabled true --share-type ORG
use_when: When the agent needs to generate or revoke an external share link for a chart.
source: internal/helpers/aitable.go:6834
visible_flags: 6

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --chart-id <String>: 目标 Chart ID (必填)
- --enabled <String>: 分享开关：true 开启，false 关闭 (必填)
- --share-type <String>: 分享类型：PUBLIC 或 ORG（enabled=true 时生效）
- --allow-back-to-doc <Bool>: 是否允许从分享页返回源 AI 表格（仅在显式传参时生效）

## Related
- dws aitable chart share get
