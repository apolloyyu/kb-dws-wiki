# dws mail +template-update

kind: shortcut
completeness: full
description: 更新草稿模板并按原 ID 读回验证
source: internal/shortcut/mail/writes.go:377
visible_flags: 5

## Flags
- --email <String>: —
- --id <String>: —
- --name <String>: 新模板名称
- --subject <String>: 新主题
- --body <String>: 新正文

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
