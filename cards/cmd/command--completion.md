# dws completion

kind: command
completeness: partial
usage: dws completion [bash|zsh|fish]
description: 生成 Shell 自动补全脚本
example: dws completion zsh > "${fpath[1]}/_dws"
source: internal/app/completion_command.go:21
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- none
