# dws mail contact batch-delete

kind: command
completeness: full
description: 批量删除邮件
source: internal/helpers/mail.go:1648
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --ids <String>: 要删除的邮件 ID 列表，逗号分隔 (必填)

## Related
- dws mail contact create
- dws mail contact list
- dws mail contact update
