# dws aitable dashboard create

kind: command
completeness: full
usage: dws aitable dashboard create
description: Create a new dashboard inside a Base with a layout of chart widgets.
example: dws aitable dashboard create --base-id BASE_ID --name "销售看板"
use_when: When the agent wants to group multiple charts into a single dashboard view for a report or overview page.
source: internal/helpers/aitable.go:6241
visible_flags: 3

## Flags
- --base-id <String>: 所属 Base ID (必填)
- --config <String>: Dashboard 配置 JSON，结构参考 dashboard config-example。可用 --name 替代来快速创建空看板
- --name <String>: 新仪表盘名称（替代 --config 简化版创建空看板）

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard delete
- dws aitable dashboard get
- dws aitable dashboard share
- dws aitable dashboard update
