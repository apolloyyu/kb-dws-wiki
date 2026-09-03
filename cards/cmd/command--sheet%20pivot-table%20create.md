# dws sheet pivot-table create

kind: command
completeness: full
description: 创建透视表
source: internal/helpers/sheet_pivot_table.go:196
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --source <String>: 数据源区域，A1 表示法且包含工作表前缀 (必填)
- --properties <String>: 透视表配置 JSON 或 @文件路径 (必填)
- --target-sheet-id <String>: 目标工作表 ID 或名称 (可选，不传则自动新建)
- --target-position <String>: 透视表放置位置，A1 单元格地址 (可选)

## Related
- dws sheet pivot-table delete
- dws sheet pivot-table list
- dws sheet pivot-table update
