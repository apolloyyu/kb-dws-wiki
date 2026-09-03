# dws aitable base list

kind: command
completeness: full
description: List AI tables (Bases) accessible to the current user, paginated.
use_when: When the agent needs to enumerate the user's Bases to pick one by name or index.
source: internal/helpers/aitable.go:1722
visible_flags: 2

## Flags
- --limit <Int>: 每页数量，默认 10，最大 10
- --cursor <String>: 首次不传；传入上次返回的游标继续获取下一页

## Related
- dws aitable base copy
- dws aitable base create
- dws aitable base delete
- dws aitable base get
- dws aitable base get-primary-doc-id
- dws aitable base search
