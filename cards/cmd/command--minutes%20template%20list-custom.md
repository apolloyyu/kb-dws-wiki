# dws minutes template list-custom

kind: command
completeness: partial
usage: dws minutes template list-custom
description: —
source: internal/helpers/minutes.go:2350
visible_flags: 2
partial_reason: missing_description

## Flags
- --limit <Int>: 每页数量，整数1-10，默认5
- --cursor <String>: 上一页meta.pagination.next_token；首页省略，不能空白

## Related
- dws minutes template create
- dws minutes template delete
- dws minutes template list-system
- dws minutes template set-default
- dws minutes template update
