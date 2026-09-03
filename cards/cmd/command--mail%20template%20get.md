# dws mail template get

kind: command
completeness: full
usage: dws mail template get
description: 获取邮件模板详情
example: dws mail template get --email user@company.com --id <templateId>
source: internal/helpers/mail.go:2867
visible_flags: 2

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --id <String>: 模板唯一标识 (必填)

## Related
- dws mail template create
- dws mail template delete
- dws mail template list
- dws mail template update
