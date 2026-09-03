# dws mail thread get

kind: command
completeness: full
usage: dws mail thread get
description: 获取会话详情
example: dws mail thread get --email user@company.com --id <conversationId>
source: internal/helpers/mail.go:1064
visible_flags: 2

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --id <String>: 会话唯一标识 conversationId (必填)

## Related
- dws mail thread batch-trash
- dws mail thread batch-update
- dws mail thread list
- dws mail thread trash
- dws mail thread update
