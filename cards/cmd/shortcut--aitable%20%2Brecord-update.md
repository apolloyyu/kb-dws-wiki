# dws aitable +record-update

kind: shortcut
completeness: full
usage: dws aitable +record-update
description: 批量更新记录，自动按 100 条分片并逐批读回验证
source: internal/shortcut/aitable/aitable.go:770
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --records <String>: 记录 JSON 数组，如 '[{\"recordId\":\"rec\",\"cells\":{...}}]'

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
