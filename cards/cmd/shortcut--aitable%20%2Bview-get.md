# dws aitable +view-get

kind: shortcut
completeness: full
usage: dws aitable +view-get
description: 获取视图完整信息（列顺序、筛选、排序、分组等）
source: internal/shortcut/aitable/aitable.go:1177
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --view-ids <StringSlice>: View ID 列表，单次最多 10 个（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
