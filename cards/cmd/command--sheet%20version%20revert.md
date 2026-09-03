# dws sheet version revert

kind: command
completeness: full
description: [危险] 回滚表格到指定历史版本或 revision
source: internal/helpers/sheet_version.go:113
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --version <Int>: 目标历史版本或已确认 revision (必填，通常从 version list 获取)

## Related
- dws sheet version list
- dws sheet version save
