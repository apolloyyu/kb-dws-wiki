# dws wiki space delete

kind: command
completeness: full
usage: dws wiki space delete
description: 删除知识库
example: dws wiki space delete --workspace <workspaceId>
source: internal/helpers/wiki.go:464
visible_flags: 1

## Flags
- --workspace <String>: 知识库 ID 或 URL (必填)

## Related
- dws wiki space create
- dws wiki space get
- dws wiki space list
- dws wiki space search
