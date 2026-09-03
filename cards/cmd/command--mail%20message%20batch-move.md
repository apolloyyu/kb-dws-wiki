# dws mail message batch-move

kind: command
completeness: full
usage: dws mail message batch-move
description: 批量移动邮件到指定文件夹
example: dws mail message batch-move --email user@company.com --ids <id1>,<id2> --folder 6
source: internal/helpers/mail.go:1596
visible_flags: 3

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --ids <String>: 要移动的邮件 ID 列表，逗号分隔 (必填)
- --folder <String>: 目标文件夹 ID (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-update
- dws mail message export
- dws mail message forward
- dws mail message get
