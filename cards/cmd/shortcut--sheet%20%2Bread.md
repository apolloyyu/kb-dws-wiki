# dws sheet +read

kind: shortcut
completeness: full
description: 完整读取并严格校验在线电子表格范围；截断结果失败关闭
source: internal/shortcut/sheet/sheet.go:159
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL；--node 去除空白后不能为空
- --sheet-id <String>: 工作表 ID 或名称 (不传则第一个工作表)；显式传入时去除空白后不能为空
- --range <String>: 读取范围，A1 表示法 (不传则全部数据)；显式传入时去除空白后不能为空
- --value-render-option <String>: 取值模式

## Related
- dws sheet +list-sheets
