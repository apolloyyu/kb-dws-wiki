# dws wiki space get

kind: command
completeness: full
usage: dws wiki space get
description: 查看知识库详情
example: dws wiki space get --workspace <workspaceId>
source: internal/helpers/wiki.go:240
visible_flags: 1

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)

## Related
- dws wiki space create
- dws wiki space delete
- dws wiki space list
- dws wiki space search
