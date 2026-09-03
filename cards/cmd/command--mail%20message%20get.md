# dws mail message get

kind: command
completeness: full
usage: dws mail message get
description: 查看邮件完整内容
example: dws mail message get --email user@company.com --id <messageId>
source: internal/helpers/mail.go:449
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 邮件 ID (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
