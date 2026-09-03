# dws mail block-list remove

kind: command
completeness: full
usage: dws mail block-list remove
description: 移除个人收信黑名单
example: dws mail block-list remove --email user@company.com --entries spam@bad.com,@junk.com
source: internal/helpers/mail.go:3696
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --entries <String>: 逗号分隔的地址列表，支持邮件地址(如123@domain.com)或域名(如@domain.com)

## Related
- dws mail block-list add
- dws mail block-list list
