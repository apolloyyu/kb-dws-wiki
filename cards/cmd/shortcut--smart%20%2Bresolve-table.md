# dws smart +resolve-table

kind: shortcut
completeness: full
description: 在某个多维表 Base 内按名称解析出唯一的数据表 tableId（只读）
source: internal/shortcut/smart/resolve_table.go:47
visible_flags: 3

## Flags
- --base <String>: Base ID（要在其内解析数据表的多维表）
- --name <String>: 要解析的数据表名称
- --fuzzy <Bool>: —

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
