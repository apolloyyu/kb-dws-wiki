# dws sheet csv-get

kind: command
completeness: full
description: 以 CSV 格式读取工作表数据
source: internal/helpers/sheet_data.go:399
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称
- --range <String>: 读取范围，A1 表示法 (不传则读取全部非空数据)
- --value-render-option <String>: 取值模式: formatted_value | raw_value | formula
- --max-chars <Int>: CSV 最大字符数 (默认 200000)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
