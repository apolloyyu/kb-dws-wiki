# dws aitable +record-batch-create

kind: shortcut
completeness: full
usage: dws aitable +record-batch-create
description: 批量新增记录，100 条分片并按返回 ID 独立验证；已有 recordId 明确拒绝
source: internal/shortcut/aitable/parity_create.go:23
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --records <String>: 非空 records JSON 数组，每项 cells；不允许 recordId，最多 10000 项

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
