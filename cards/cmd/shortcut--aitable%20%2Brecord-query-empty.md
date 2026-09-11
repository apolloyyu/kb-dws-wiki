# dws aitable +record-query-empty

kind: shortcut
completeness: full
usage: dws aitable +record-query-empty
description: 扫描并过滤出完全没填用户字段的空行
source: internal/shortcut/aitable/aitable.go:824
visible_flags: 4

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --limit <Int>: 单次扫描预算，范围 [1,100]（可选）
- --cursor <String>: 分页游标（可选）；首次不传，后续原样使用上一页 nextCursor；records 为空不是错误，nextCursor 非空则继续扫，为空表示已扫完全表并正常完成

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
