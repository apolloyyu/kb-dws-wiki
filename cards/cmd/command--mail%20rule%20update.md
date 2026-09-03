# dws mail rule update

kind: command
completeness: full
usage: dws mail rule update
description: 更新个人收信规则
example: dws mail rule update --email user@company.com --id <ruleId> --name "新规则名" --enabled true
source: internal/helpers/mail.go:3483
visible_flags: 6

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 规则 ID (必填)
- --name <String>: 规则名称 (必填)
- --enabled <String>: 是否启用: true/false (必填)
- --conditions <String>: 规则条件 JSON 数组 (可选，为空表示命中所有邮件)
- --actions <String>: 规则动作 JSON 数组 (必填)

## Related
- dws mail rule adjust
- dws mail rule create
- dws mail rule delete
- dws mail rule list
