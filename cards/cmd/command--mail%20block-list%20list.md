# dws mail block-list list

kind: command
completeness: full
usage: dws mail block-list list
description: 列出个人收信黑名单
example: dws mail block-list list --email user@company.com
source: internal/helpers/mail.go:3657
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail block-list add
- dws mail block-list remove
