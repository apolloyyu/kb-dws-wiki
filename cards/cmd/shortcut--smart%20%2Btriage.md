# dws smart +triage

kind: shortcut
completeness: full
description: 列出或筛选邮件摘要，自动解析邮箱与收件箱
source: internal/shortcut/smart/triage_mail.go:18
visible_flags: 4

## Flags
- --query <String>: 可选 KQL 条件；不传时列出收件箱
- --email <String>: 邮箱地址；不传时自动取当前身份首个邮箱
- --limit <Int>: —
- --cursor <String>: 分页游标

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
