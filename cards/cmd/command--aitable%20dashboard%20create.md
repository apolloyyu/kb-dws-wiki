# dws aitable dashboard create

kind: command
completeness: full
description: Create a new dashboard inside a Base with a layout of chart widgets.
use_when: When the agent wants to group multiple charts into a single dashboard view for a report or overview page.
source: internal/helpers/aitable.go:1849
visible_flags: 3

## Flags
- --name <String>: Base 名称，1-50 字符；会去除首尾空格后校验 (必填)
- --folder-id <String>: 目标父节点的 dentryUuid (知识库节点 ID)，也可传入标准节点 URL，MCP 会在创建前解析出实际生效的节点 ID
- --template-id <String>: 创建 Base 模板 ID，默认创建一个空 Base。可通过 template search 获取模板

## Related
- dws aitable dashboard arrange
- dws aitable dashboard config-example
- dws aitable dashboard delete
- dws aitable dashboard get
- dws aitable dashboard update
