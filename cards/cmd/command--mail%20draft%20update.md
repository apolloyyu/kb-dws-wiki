# dws mail draft update

kind: command
completeness: full
usage: dws mail draft update
description: 更新草稿
example: dws mail draft update --from user@company.com --id <messageId> --subject "新标题" --content "新正文"
source: internal/helpers/mail.go:1894
visible_flags: 8

## Flags
- --from <String>: 发件人邮箱 (必填)
- --id <String>: 草稿邮件 ID (必填)
- --to <String>: 收件人列表
- --cc <String>: 抄送人列表
- --subject <String>: 邮件标题
- --content <String>: 邮件正文
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail draft create
- dws mail draft send
