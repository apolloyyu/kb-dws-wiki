# dws mail draft create

kind: command
completeness: full
usage: dws mail draft create
description: 创建草稿
example: dws mail draft create --from user@company.com --to colleague@company.com --subject "草稿标题" --content "草稿正文"
source: internal/helpers/mail.go:1805
visible_flags: 7

## Flags
- --from <String>: 发件人邮箱 (必填)
- --to <String>: 收件人列表
- --cc <String>: 抄送人列表
- --subject <String>: 邮件标题 (必填)
- --content <String>: 邮件正文
- --attachment <StringArray>: 附件文件路径，可多次指定 (可选)
- --inline-attachment <StringArray>: 内联附件文件路径（如图片），可多次指定，cid 自动生成 (可选)

## Related
- dws mail draft send
- dws mail draft update
