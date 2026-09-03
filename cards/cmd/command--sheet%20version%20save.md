# dws sheet version save

kind: command
completeness: full
usage: dws sheet version save
description: 手动保存表格版本快照
example: dws sheet version save --node SHEET_ID
source: internal/helpers/sheet_version.go:18
visible_flags: 1

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)

## Related
- dws sheet version list
- dws sheet version revert
