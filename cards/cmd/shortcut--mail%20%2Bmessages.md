# dws mail +messages

kind: shortcut
completeness: full
usage: dws mail +messages
description: 按请求顺序读取多封邮件并逐封验证身份
source: internal/shortcut/mail/reads.go:137
visible_flags: 2

## Flags
- --ids <StringSlice>: —
- --email <String>: 邮箱地址；不传时自动取当前身份首个邮箱

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +tag-list
