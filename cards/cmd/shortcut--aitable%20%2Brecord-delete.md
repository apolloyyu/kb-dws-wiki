# dws aitable +record-delete

kind: shortcut
completeness: full
usage: dws aitable +record-delete
description: 批量删除记录（不可逆），自动按 100 条分片并逐批确认记录已不存在
source: internal/shortcut/aitable/aitable.go:787
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-ids <StringSlice>: 待删除记录 ID 列表，逗号分隔；最多 10000 个唯一 ID

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
