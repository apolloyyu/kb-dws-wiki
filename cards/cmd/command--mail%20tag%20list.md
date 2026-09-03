# dws mail tag list

kind: command
completeness: full
usage: dws mail tag list
description: 列举邮件标签
example: dws mail tag list --email user@company.com
source: internal/helpers/mail.go:853
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail tag create
- dws mail tag delete
- dws mail tag update
