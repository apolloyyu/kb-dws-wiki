# dws mail contact batch-delete

kind: command
completeness: full
usage: dws mail contact batch-delete
description: 批量删除邮件联系人
example: dws mail contact batch-delete --email user@company.com --contact-ids <id1>,<id2>
source: internal/helpers/mail.go:3272
visible_flags: 2

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --contact-ids <String>: 要删除的联系人 ID 列表，逗号分隔 (必填)

## Related
- dws mail contact create
- dws mail contact list
- dws mail contact update
