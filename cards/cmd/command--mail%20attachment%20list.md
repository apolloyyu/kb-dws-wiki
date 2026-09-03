# dws mail attachment list

kind: command
completeness: full
usage: dws mail attachment list
description: 列举邮件附件
example: dws mail attachment list --email user@company.com --id <messageId>
source: internal/helpers/mail.go:1986
visible_flags: 2

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --id <String>: 邮件唯一标识 messageId (必填)

## Related
- dws mail attachment download
