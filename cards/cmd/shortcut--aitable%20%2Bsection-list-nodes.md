# dws aitable +section-list-nodes

kind: shortcut
completeness: full
usage: dws aitable +section-list-nodes
description: 列出指定 Base 当前版本下的全部 nsheet 节点
source: internal/shortcut/aitable/aitable.go:3177
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --type <String>: 仅返回指定 nodeType；使用目录实际返回的类型值
- --parent-id <String>: 仅返回该父分区直接子项；显式空值筛根目录

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
