# dws aitable section rename

kind: command
completeness: full
description: 重命名文件夹
source: internal/helpers/aitable.go:7537
visible_flags: 3

## Flags
- --base-id <String>: Base ID (必填)
- --section-id <String>: 目标文件夹 ID (必填)
- --new-name <String>: 新的文件夹名称 (必填)

## Related
- dws aitable section create
- dws aitable section delete
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section move-node
- dws aitable section reorder
