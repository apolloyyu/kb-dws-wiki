# dws sheet ungroup-dimension

kind: command
completeness: full
usage: dws sheet ungroup-dimension
description: 取消指定连续行/列分组
example: dws sheet ungroup-dimension --node NODE_ID --sheet-id SHEET_ID --range "3:7"
source: internal/helpers/sheet_dimension.go:736
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: C:F

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
