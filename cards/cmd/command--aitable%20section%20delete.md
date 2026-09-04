# dws aitable section delete

kind: command
completeness: full
usage: dws aitable section delete
description: 删除文件夹
example: dws aitable section delete --base-id BASE_ID --section-id SECTION_ID
source: internal/helpers/aitable.go:7594
visible_flags: 2

## Flags
- --base-id <String>: Base ID (必填)
- --section-id <String>: 目标文件夹 ID (必填)

## Related
- dws aitable section create
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section move-node
- dws aitable section rename
- dws aitable section reorder
