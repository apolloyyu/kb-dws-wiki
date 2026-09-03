# dws mail +draft-edit

kind: shortcut
completeness: full
usage: dws mail +draft-edit
description: 更新已有草稿并精确读回验证
source: internal/shortcut/mail/writes.go:255
visible_flags: 6

## Flags
- --from <String>: —
- --id <String>: —
- --to <StringSlice>: 新收件邮箱
- --cc <StringSlice>: 新抄送邮箱
- --subject <String>: 新主题
- --body <String>: 新正文

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +folder-list
- dws mail +message
- dws mail +messages
- dws mail +tag-list
