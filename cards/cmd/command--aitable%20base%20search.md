# dws aitable base search

kind: command
completeness: partial
usage: dws aitable base search
description: Search AI tables (Bases) the current user can access by keyword against the Base name.
example: dws aitable base search --query "项目管理"
use_when: When the agent knows a partial Base name and needs to resolve it to a Base ID.
source: internal/helpers/aitable.go:1765
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --query <String>: Base 名称关键词，建议至少 2 个字符 (必填)
- --cursor <String>: 分页游标，首次不传

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base list
