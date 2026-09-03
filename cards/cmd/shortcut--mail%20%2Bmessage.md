# dws mail +message

kind: shortcut
completeness: full
description: 读取一封邮件的完整正文与附件元数据
source: internal/shortcut/mail/reads.go:110
visible_flags: 2

## Flags
- --id <String>: —
- --email <String>: 邮箱地址；不传时自动取当前身份首个邮箱

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +messages
- dws mail +tag-list
