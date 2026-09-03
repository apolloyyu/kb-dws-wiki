# dws aitable +table-get

kind: shortcut
completeness: full
usage: dws aitable +table-get
description: 批量获取指定数据表的表级信息、字段目录与视图目录
source: internal/shortcut/aitable/aitable.go:441
visible_flags: 2

## Flags
- --base-id <String>: Base ID
- --table-ids <StringSlice>: Table ID 列表，逗号分隔，单次最多 10 个（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
