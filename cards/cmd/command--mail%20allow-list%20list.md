# dws mail allow-list list

kind: command
completeness: full
usage: dws mail allow-list list
description: 列出个人收信白名单
example: dws mail allow-list list --email user@company.com
source: internal/helpers/mail.go:3589
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail allow-list add
- dws mail allow-list remove
