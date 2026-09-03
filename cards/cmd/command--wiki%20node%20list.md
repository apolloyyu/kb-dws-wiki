# dws wiki node list

kind: command
completeness: full
usage: dws wiki node list
description: 列出知识库节点
example: dws wiki node list --workspace <workspaceId>
source: internal/helpers/wiki.go:971
visible_flags: 4

## Flags
- --workspace <String>: 知识库 ID (必填)
- --folder <String>: 父节点 nodeId (选填，不传则列出根目录)
- --limit <Int>: 每页数量 (默认 50，最大 50)
- --cursor <String>: 分页游标

## Related
- dws wiki node copy
- dws wiki node create
- dws wiki node delete
- dws wiki node move
- dws wiki node search
