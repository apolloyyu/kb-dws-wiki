# dws chat group list-join-validations

kind: command
completeness: full
usage: dws chat group list-join-validations
description: 分页拉取入群验证记录
example: dws chat group list-join-validations
source: internal/helpers/chat.go:9443
visible_flags: 2

## Flags
- --limit <Int>: 单页数量（默认 20，最大 50）
- --cursor <String>: 分页游标（首次不传，翻页传返回的 nextCursor）

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
