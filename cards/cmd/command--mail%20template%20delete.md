# dws mail template delete

kind: command
completeness: full
description: 删除邮件文件夹
source: internal/helpers/mail.go:724
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 要删除的邮件文件夹 ID (必填)

## Related
- dws mail template create
- dws mail template get
- dws mail template list
- dws mail template update
