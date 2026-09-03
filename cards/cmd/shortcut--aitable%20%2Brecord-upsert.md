# dws aitable +record-upsert

kind: shortcut
completeness: full
description: 按 recordId 自动拆分 create/update，按 100 条分片并读回验证
source: internal/shortcut/aitable/aitable.go:969
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --records <String>: 记录 JSON 数组，单次最多 100 条

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
