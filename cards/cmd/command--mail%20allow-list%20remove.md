# dws mail allow-list remove

kind: command
completeness: full
usage: dws mail allow-list remove
description: 移除个人收信白名单
example: dws mail allow-list remove --email user@company.com --entries a@b.com,@spam.com
source: internal/helpers/mail.go:3628
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --entries <String>: 逗号分隔的地址列表，支持邮件地址(如123@domain.com)或域名(如@domain.com)

## Related
- dws mail allow-list add
- dws mail allow-list list
