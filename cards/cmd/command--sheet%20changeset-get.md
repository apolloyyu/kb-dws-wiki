# dws sheet changeset-get

kind: command
completeness: partial
usage: dws sheet changeset-get
description: —
source: internal/helpers/sheet_revision.go:284
visible_flags: 3
partial_reason: missing_description

## Flags
- --node <String> required: 表格文档 ID 或 URL (必填)
- --start-revision <String> required: 查询基线 revision (必填，非负；结果不包含该 revision)
- --end-revision <String>: 查询结束 revision (可选，非负；结果包含该 revision)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet chart
- dws sheet comment
- dws sheet cond-format
