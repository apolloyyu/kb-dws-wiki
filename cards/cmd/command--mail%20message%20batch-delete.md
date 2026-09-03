# dws mail message batch-delete

kind: command
completeness: full
usage: dws mail message batch-delete
description: 批量删除邮件
example: dws mail message batch-delete --email user@company.com --ids <id1>,<id2>
source: internal/helpers/mail.go:1648
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --ids <String>: 要删除的邮件 ID 列表，逗号分隔 (必填)

## Related
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
- dws mail message get
