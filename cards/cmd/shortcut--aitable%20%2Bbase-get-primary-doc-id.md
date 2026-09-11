# dws aitable +base-get-primary-doc-id

kind: shortcut
completeness: full
usage: dws aitable +base-get-primary-doc-id
description: 根据 baseId/tableId/recordId 查询主键文档是否存在及其 dentryUuid
source: internal/shortcut/aitable/aitable.go:349
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: 记录 ID

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
