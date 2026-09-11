# dws aitable chart create

kind: command
completeness: full
usage: dws aitable chart create
description: Create a new chart inside a Base, bound to a datasheet and view with a given configuration.
example: dws aitable chart create --base-id BASE_ID --dashboard-id DASHBOARD_ID
use_when: When the agent is building analytics on top of a datasheet and needs to materialize a chart visualization.
source: internal/helpers/aitable.go:7765
visible_flags: 5

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --dashboard-id <String>: 所属 Dashboard ID (必填)
- --config <String>: 图表配置 JSON，结构参考 chart widgets-example (必填)
- --layout <String>: 图表布局 JSON，如 {\"x\":0,\"y\":0,\"w\":6,\"h\":4} (必填)
- --is-app-mode <Bool>: 只读应用模式上下文：仅已确认应用模式时传 --is-app-mode=true，强制按 48 列校验；不会写入 MCP payload

## Related
- dws aitable chart delete
- dws aitable chart get
- dws aitable chart share
- dws aitable chart update
- dws aitable chart widgets-example
