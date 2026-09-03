# dws mail block-list add

kind: command
completeness: full
usage: dws mail block-list add
description: 添加个人收信黑名单
example: dws mail block-list add --email user@company.com --entries spam@bad.com,@junk.com
source: internal/helpers/mail.go:3677
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --entries <String>: 逗号分隔的地址列表，支持邮件地址(如123@domain.com)或域名(如@domain.com)

## Related
- dws mail block-list list
- dws mail block-list remove
