# dws aitable +record-bulk-patch

kind: shortcut
completeness: full
description: 完整查询目标记录后批量合并同一组 cells，自动分片并逐条读回验证
source: internal/shortcut/aitable/record_bulk_patch.go:17
visible_flags: 9

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --patch <String>: 要合并到每条记录的非空 cells JSON 对象
- --filters <String>: query_records filters JSON（选择条件之一）
- --query <String>: 全文关键词（选择条件之一）
- --record-ids <StringSlice>: 明确的 recordId 列表（选择条件之一）
- --view-id <String>: 可选视图上下文
- --all <Bool>: 明确允许匹配整张表
- --max-matches <Int>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
