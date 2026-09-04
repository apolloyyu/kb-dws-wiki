# dws aitable dashboard share update

kind: command
completeness: full
usage: dws aitable dashboard share update
description: Enable, disable, or update the public-sharing configuration of a dashboard.
example: dws aitable dashboard share update --base-id BASE_ID --dashboard-id DASHBOARD_ID --enabled true --share-type PUBLIC
use_when: When the agent needs to generate or revoke an external share link for a dashboard.
source: internal/helpers/aitable.go:6504
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 目标 Dashboard ID (必填)
- --enabled <String>: 分享开关：true 开启，false 关闭 (必填)
- --share-type <String>: 分享类型：PUBLIC 或 ORG（enabled=true 时生效）
- --allow-back-to-doc <Bool>: 是否允许从分享页返回源 AI 表格（仅在显式传参时生效）

## Related
- dws aitable dashboard share get
