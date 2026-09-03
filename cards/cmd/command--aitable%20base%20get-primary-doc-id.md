# dws aitable base get-primary-doc-id

kind: command
completeness: full
description: 获取主键文档ID
source: internal/helpers/aitable.go:1679
visible_flags: 3

## Flags
- --base-id <String>: Base ID，可通过 list_bases 或 search_bases 获取 (必填)
- --table-id <String>: Table ID，可通过 list_tables 或 get_base 获取 (必填)
- --record-id <String>: 记录 ID (必填)

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base list
- dws aitable base search
