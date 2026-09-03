# dws mail +draft-create

kind: shortcut
completeness: full
usage: dws mail +draft-create
description: 创建邮件草稿并按 messageId 读回验证
source: internal/shortcut/mail/writes.go:191
visible_flags: 5

## Flags
- --from <String>: —
- --to <StringSlice>: 收件邮箱，可多次指定或逗号分隔
- --cc <StringSlice>: 抄送邮箱，可多次指定或逗号分隔
- --subject <String>: —
- --body <String>: 草稿正文

## Related
- dws mail +contact-list
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
- dws mail +tag-list
