# dws mail thread trash

kind: command
completeness: full
usage: dws mail thread trash
description: [危险] 删除邮件会话
example: dws mail thread trash --email user@company.com --id <conversationId> --yes
source: internal/helpers/mail.go:1216
visible_flags: 3

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --id <String>: 要删除的会话 ID (必填)
- --yes <Bool>: 确认执行此危险操作 (必填)

## Related
- dws mail thread batch-trash
- dws mail thread batch-update
- dws mail thread get
- dws mail thread list
- dws mail thread update
