# dws aitable +data-query

kind: shortcut
completeness: full
usage: dws aitable +data-query
description: 用 DWS JSON DSL 统一执行标量或分组聚合，不拉全表做本地统计
source: internal/shortcut/aitable/parity_stats.go:15
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --table-id <String>: Table ID
- --dsl <String>: DWS DSL 对象：stats 为 1-20 项 fieldId/statsType；可选 group/filters/sort/dataVersion/keyword；不接受 limit 以免静默统计子集

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
