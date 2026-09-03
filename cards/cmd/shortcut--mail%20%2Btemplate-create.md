# dws mail +template-create

kind: shortcut
completeness: full
usage: dws mail +template-create
description: 创建个人邮件模板并按模板 ID 读回
source: internal/shortcut/mail/writes.go:328
visible_flags: 5

## Flags
- --email <String>: —
- --name <String>: —
- --subject <String>: —
- --body <String>: —
- --is-draft <Bool>: 是否创建可编辑的草稿模板；默认 false

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
