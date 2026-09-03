# dws mail rule delete

kind: command
completeness: full
usage: dws mail rule delete
description: 删除个人收信规则
example: dws mail rule delete --email user@company.com --id <ruleId>
source: internal/helpers/mail.go:3526
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 规则 ID (必填)

## Related
- dws mail rule adjust
- dws mail rule create
- dws mail rule list
- dws mail rule update
