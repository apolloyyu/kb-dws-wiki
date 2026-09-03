# dws mail message list

kind: command
completeness: full
usage: dws mail message list
description: 列出文件夹中的邮件
example: dws mail message list --email user@company.com
source: internal/helpers/mail.go:374
visible_flags: 4

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --folder-id <String>: 文件夹 ID（1=已发送, 2=收件箱, 3=垃圾邮件, 5=草稿, 6=已删除），默认为收件箱
- --limit <String>: 每页返回数量(最大限制 100, 默认 20)
- --cursor <String>: 邮件的起始偏移标识, 其值取自响应中的nextCursor字段

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
