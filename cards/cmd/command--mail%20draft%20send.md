# dws mail draft send

kind: command
completeness: full
description: 发送邮件
source: internal/helpers/mail.go:501
visible_flags: 7

## Flags
- --from <String>: 发件人邮箱 (必填)
- --to <String>: 收件人列表 (必填)
- --subject <String>: 邮件标题 (必填)
- --content <String>: 邮件正文 (必填)
- --cc <String>: 抄送人列表
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail draft create
- dws mail draft update
