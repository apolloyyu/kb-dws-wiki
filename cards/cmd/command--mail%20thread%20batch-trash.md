# dws mail thread batch-trash

kind: command
completeness: full
usage: dws mail thread batch-trash
description: [危险] 批量删除邮件会话
example: dws mail thread batch-trash --email user@company.com --ids <conversationId1>,<conversationId2> --yes
source: internal/helpers/mail.go:1247
visible_flags: 3

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --ids <String>: 要删除的会话 ID 列表，多个用英文逗号分隔，最多 100 个 (必填)
- --yes <Bool>: 确认执行此危险操作 (必填)

## Related
- dws mail thread batch-update
- dws mail thread get
- dws mail thread list
- dws mail thread trash
- dws mail thread update
