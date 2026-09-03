# dws aitable +base-schema-snapshot

kind: shortcut
completeness: full
usage: dws aitable +base-schema-snapshot
description: 读取 Base、全部数据表、字段和视图的可复用结构快照，并严格校验每层响应
source: internal/shortcut/aitable/base_composite.go:18
visible_flags: 1

## Flags
- --base-id <String>: Base ID

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
