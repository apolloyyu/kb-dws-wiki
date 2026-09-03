# dws mail +thread

kind: shortcut
completeness: full
description: 读取完整邮件会话并精确验证 conversationId
source: internal/shortcut/mail/reads.go:188
visible_flags: 2

## Flags
- --id <String>: —
- --email <String>: 邮箱地址；不传时自动取当前身份首个邮箱

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
