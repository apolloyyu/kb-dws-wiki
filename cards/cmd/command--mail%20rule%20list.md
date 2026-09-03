# dws mail rule list

kind: command
completeness: full
usage: dws mail rule list
description: 列出个人收信规则
example: dws mail rule list --email user@company.com
source: internal/helpers/mail.go:3404
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail rule adjust
- dws mail rule create
- dws mail rule delete
- dws mail rule update
