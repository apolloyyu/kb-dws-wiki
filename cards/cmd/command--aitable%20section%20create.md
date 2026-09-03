# dws aitable section create

kind: command
completeness: full
usage: dws aitable section create
description: 创建文件夹
example: dws aitable section create --base-id BASE_ID --name 我的文件夹
source: internal/helpers/aitable.go:7482
visible_flags: 4

## Flags
- --base-id <String>: Base ID (必填)
- --name <String>: 文件夹名称 (必填)
- --parent-section-id <String>: 父文件夹 ID；不传或空字符串表示创建在 Base 根目录下
- --index <Int>: 在父文件夹下的目标位置（0-based）；不传则追加到末尾

## Related
- dws aitable section delete
- dws aitable section list-empty
- dws aitable section list-nodes
- dws aitable section move-node
- dws aitable section rename
- dws aitable section reorder
