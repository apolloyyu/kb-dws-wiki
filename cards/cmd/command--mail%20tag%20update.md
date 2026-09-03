# dws mail tag update

kind: command
completeness: full
usage: dws mail tag update
description: 更新邮件标签
example: dws mail tag update --email user@company.com --id <tagId> --name "新标签名"
source: internal/helpers/mail.go:962
visible_flags: 3

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 要更新的邮件标签 ID (必填)
- --name <String>: 更新后的邮件标签名称 (必填)

## Related
- dws mail tag create
- dws mail tag delete
- dws mail tag list
