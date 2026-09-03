# dws mail auto-reply get

kind: command
completeness: full
usage: dws mail auto-reply get
description: 获取用户的自动回复配置
example: dws mail auto-reply get --email user@company.com
source: internal/helpers/mail.go:3326
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail auto-reply update
