# dws mail message get

kind: command
completeness: full
description: 查看邮件完整内容
source: internal/helpers/mail.go:449
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 邮件 ID (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-move
- dws mail message export
- dws mail message forward
- dws mail message list
- dws mail message reply
