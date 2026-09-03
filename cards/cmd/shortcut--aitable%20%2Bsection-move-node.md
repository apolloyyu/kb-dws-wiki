# dws aitable +section-move-node

kind: shortcut
completeness: full
description: 把任意 nsheet 节点移动到目标文件夹下（可选调整位置）
source: internal/shortcut/aitable/aitable.go:3098
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --node-id <String>: 待移动节点 ID
- --new-parent-section-id <String>: 目标父文件夹 ID，空字符串表示 Base 根目录
- --target-index <Int>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
