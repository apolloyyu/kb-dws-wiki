# dws aitable +base-get-primary-doc-id

kind: shortcut
completeness: full
usage: dws aitable +base-get-primary-doc-id
description: 根据 baseId/tableId/recordId 获取主键文档的 dentryUuid
source: internal/shortcut/aitable/aitable.go:345
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
