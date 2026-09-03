# dws mail sent-message recall-detail

kind: command
completeness: full
usage: dws mail sent-message recall-detail
description: 查询邮件撤回进度
example: dws mail sent-message recall-detail --email user@company.com --id <recallTaskId>
source: internal/helpers/mail.go:2484
visible_flags: 2

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 撤回任务 ID (必填)，由 recall 命令返回

## Related
- dws mail sent-message recall
