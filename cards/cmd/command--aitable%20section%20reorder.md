# dws aitable section reorder

kind: command
completeness: full
usage: dws aitable section reorder
description: 调整文件夹顺序
example: dws aitable section reorder --base-id BASE_ID --section-id SECTION_ID --target-index 0
source: internal/helpers/aitable.go:7626
visible_flags: 3

## Flags
- --base-id <String>: Base ID (必填)
- --section-id <String>: 目标文件夹 ID (必填)
- --target-index <Int>: 目标位置（0-based）(必填)

## Related
- dws aitable section create
- dws aitable section delete
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section move-node
- dws aitable section rename
