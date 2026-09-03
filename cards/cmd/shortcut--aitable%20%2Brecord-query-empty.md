# dws aitable +record-query-empty

kind: shortcut
completeness: full
usage: dws aitable +record-query-empty
description: 扫描并过滤出完全没填用户字段的空行
source: internal/shortcut/aitable/aitable.go:804
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --limit <Int>: 单次扫描预算，范围 [1,100]（可选）
- --cursor <String>: 分页游标（可选）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
