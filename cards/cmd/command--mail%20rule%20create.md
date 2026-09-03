# dws mail rule create

kind: command
completeness: full
usage: dws mail rule create
description: 创建个人收信规则
example: dws mail rule create --email user@company.com --name "VIP邮件标记" --enabled true
source: internal/helpers/mail.go:3426
visible_flags: 5

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --name <String>: 规则名称 (必填)
- --enabled <String>: 是否启用: true/false (必填)
- --conditions <String>: 规则条件 JSON 数组 (可选)
- --actions <String>: 规则动作 JSON 数组 (必填)

## Related
- dws mail rule adjust
- dws mail rule delete
- dws mail rule list
- dws mail rule update
