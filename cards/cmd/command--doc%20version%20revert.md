# dws doc version revert

kind: command
completeness: full
description: 回滚文档到指定版本
source: internal/helpers/doc.go:4508
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --version <Int>: 目标版本号 (必填，从 list 获取)

## Related
- dws doc version list
- dws doc version save
