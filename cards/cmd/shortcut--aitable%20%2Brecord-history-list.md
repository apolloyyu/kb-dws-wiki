# dws aitable +record-history-list

kind: shortcut
completeness: full
usage: dws aitable +record-history-list
description: 按 recordId 查询单条记录的变更历史
source: internal/shortcut/aitable/aitable.go:859
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --record-id <String>: 记录 ID
- --offset <Int>: 分页偏移量，默认 0（可选）
- --limit <Int>: 每页数量，默认 20，最大 50（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
