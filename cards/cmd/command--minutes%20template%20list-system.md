# dws minutes template list-system

kind: command
completeness: partial
usage: dws minutes template list-system
description: —
source: internal/helpers/minutes.go:2327
visible_flags: 3
partial_reason: missing_description

## Flags
- --limit <Int>: 每页数量，整数1-50，默认20
- --cursor <String>: 上一页 meta.pagination.next_token，原样传入；首页省略
- --locale <String>: 语言区域，默认zh_CN；续页保持一致

## Related
- dws minutes template create
- dws minutes template delete
- dws minutes template list-custom
- dws minutes template set-default
- dws minutes template update
