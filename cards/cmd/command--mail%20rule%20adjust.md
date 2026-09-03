# dws mail rule adjust

kind: command
completeness: full
usage: dws mail rule adjust
description: 调整收信规则排序
example: dws mail rule adjust --email user@company.com --id <ruleId> --direction up
source: internal/helpers/mail.go:3545
visible_flags: 3

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 规则 ID (必填)
- --direction <String>: 调整方向: up/down (必填)

## Related
- dws mail rule create
- dws mail rule delete
- dws mail rule list
- dws mail rule update
