# dws sheet comment create

kind: command
completeness: full
usage: dws sheet comment create
description: 创建单元格评论
example: dws sheet comment create --node <SHEET_ID> --sheet-id Sheet1 --range A2 --content "这个数字有问题"
source: internal/helpers/sheet_comment.go:81
visible_flags: 5

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --content <String>: 评论内容 (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 单元格位置 A1 表示法 (必填)
- --mention <String>: 被 @ 的用户 uid 列表，逗号分隔

## Related
- dws sheet comment delete
- dws sheet comment list
- dws sheet comment reply
- dws sheet comment update
