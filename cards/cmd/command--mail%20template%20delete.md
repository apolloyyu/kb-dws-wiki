# dws mail template delete

kind: command
completeness: full
usage: dws mail template delete
description: 删除邮件模板
example: dws mail template delete --email user@company.com --id <templateId>
source: internal/helpers/mail.go:3013
visible_flags: 2

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --id <String>: 模板唯一标识 (必填)

## Related
- dws mail template create
- dws mail template get
- dws mail template list
- dws mail template update
