# dws sheet append

kind: command
completeness: full
usage: dws sheet append
description: 在工作表末尾追加数据
example: dws sheet append --node NODE_ID --sheet-id SHEET_ID --values '[["张三","销售部",50000]]'
source: internal/helpers/sheet_data.go:226
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --values <String>: 追加数据，二维 JSON 数组 (必填)

## Related
- dws sheet add-dimension
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
- dws sheet cond-format
