# dws aitable section move-node

kind: command
completeness: full
usage: dws aitable section move-node
description: 移动节点
example: dws aitable section move-node --base-id BASE_ID --node-id NODE_ID --new-parent-section-id SECTION_ID
source: internal/helpers/aitable.go:7768
visible_flags: 4

## Flags
- --base-id <String>: Base ID (必填)
- --node-id <String>: 要移动的节点 ID，可以是文件夹、AI表格、表单视图、仪表盘、文档或查询视图 (必填)
- --new-parent-section-id <String>: 目标父文件夹 ID；空字符串表示移到 Base 根目录 (必填)
- --target-index <Int>: Base 内节点的全局位置（0-based）；不传则不调整

## Related
- dws aitable section create
- dws aitable section delete
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section rename
- dws aitable section reorder
