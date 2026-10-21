# dws aitable +list-tables

kind: shortcut
completeness: full
usage: dws aitable +list-tables
description: 列出某个多维表(base)里的所有数据表（只读，投影 tableId/tableName）
source: internal/shortcut/smart/list_tables.go:40
visible_flags: 1

## Flags
- --base <String>: Base ID（要列出数据表的多维表）

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
