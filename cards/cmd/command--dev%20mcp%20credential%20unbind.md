# dws dev mcp credential unbind

kind: command
completeness: partial
usage: dws dev mcp credential unbind
description: 解绑发布实例的生效凭证（bind 的逆操作；credential delete 报 credential_in_use 时先走本命令）
example: dws dev mcp credential unbind --mcp-id 10520 --dry-run --format json
source: internal/helpers/dev_mcp_hsf.go:245
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws dev mcp credential list
- dws dev mcp credential save
