# dws aitable +chart-update

kind: shortcut
completeness: full
description: 更新指定 chart 的配置或布局（--config 必填）
source: internal/shortcut/aitable/aitable.go:2456
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --chart-id <String>: Chart ID
- --config <String>: 图表配置 JSON（至少含 chartName）
- --layout <String>: 布局 JSON（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
