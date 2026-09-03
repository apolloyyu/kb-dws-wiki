# dws sheet comment list

kind: command
completeness: full
description: 查询表格评论列表
source: internal/helpers/sheet_comment.go:17
visible_flags: 6

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --limit <Int>: 每页返回的评论数量，默认 50，最大 50
- --cursor <String>: 分页游标
- --resolve-status <String>: 按解决状态过滤: resolved / unresolved
- --sheet-id <String>: 工作表 ID 或名称（与 --range 一起按单元格过滤）
- --range <String>: 单元格位置 A1 表示法（与 --sheet-id 一起按单元格过滤）

## Related
- dws sheet comment create
- dws sheet comment delete
- dws sheet comment reply
- dws sheet comment update
