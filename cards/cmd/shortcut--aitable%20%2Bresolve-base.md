# dws aitable +resolve-base

kind: shortcut
completeness: full
usage: dws aitable +resolve-base
description: 按名称搜索多维表 Base 并解析出唯一 baseId（只读）
source: internal/shortcut/smart/resolve_base.go:41
visible_flags: 2

## Flags
- --name <String>: 要解析的 Base 名称
- --fuzzy <Bool>: —

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
