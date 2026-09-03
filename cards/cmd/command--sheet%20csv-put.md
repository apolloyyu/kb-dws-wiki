# dws sheet csv-put

kind: command
completeness: full
usage: dws sheet csv-put
description: 将 CSV 数据写入表格指定位置（支持公式，自动扩容）
example: dws sheet csv-put --node NODE_ID --sheet-id SHEET_ID --start-cell A1
source: internal/helpers/sheet_data.go:291
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --csv <String>: CSV 文本、@文件路径 或 - 表示 stdin (必填)
- --start-cell <String>: 起始单元格，A1 表示法 (必填)
- --auto-convert <Bool>: 自动推断非公式 CSV 字段的数字、日期、布尔等类型；设为 false 时按文本原样写入，= 开头仍作为公式
- --allow-overwrite <Bool>: 允许覆盖已有数据 (默认 false)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
