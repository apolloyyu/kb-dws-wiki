# dws config list

kind: command
completeness: full
description: 列出所有可用配置项
source: internal/app/config_command.go:42
visible_flags: 4

## Flags
- --category <String>: 按分类过滤 (core|auth|network|security|runtime|debug|external)
- --show-values <Bool>: 显示配置项的当前实际值 (敏感信息会脱敏)
- --show-hidden <Bool>: 包含隐藏的内部调试配置项
- --json <Bool>: 以 JSON 格式输出

## Related
- none
