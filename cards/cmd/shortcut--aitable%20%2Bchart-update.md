# dws aitable +chart-update

kind: shortcut
completeness: full
usage: dws aitable +chart-update
description: 更新指定 chart 的配置或布局（--config 必填；layout 写前强制校验 12/48 列协议）
source: internal/shortcut/aitable/aitable.go:2547
visible_flags: 6

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --chart-id <String>: Chart ID
- --config <String>: 图表配置 JSON（至少含 chartName）
- --layout <String>: 布局 JSON（可选）
- --is-app-mode <Bool>: 只读应用模式上下文；仅已确认应用模式且更新 layout 时传 true，不写入 MCP payload

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
