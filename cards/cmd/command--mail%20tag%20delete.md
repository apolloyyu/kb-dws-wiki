# dws mail tag delete

kind: command
completeness: full
usage: dws mail tag delete
description: 删除邮件标签
example: dws mail tag delete --email user@company.com --id <tagId>
source: internal/helpers/mail.go:936
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 要删除的邮件标签 ID (必填)

## Related
- dws mail tag create
- dws mail tag list
- dws mail tag update
