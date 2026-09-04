# dws aitable section rename

kind: command
completeness: full
usage: dws aitable section rename
description: 重命名文件夹
example: dws aitable section rename --base-id BASE_ID --section-id SECTION_ID --new-name 新名称
source: internal/helpers/aitable.go:7549
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
