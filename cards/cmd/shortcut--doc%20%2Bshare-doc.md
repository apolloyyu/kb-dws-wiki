# dws doc +share-doc

kind: shortcut
completeness: full
usage: dws doc +share-doc
description: 按姓名把文档链接私信发给某人（自动解析 userId）
source: internal/shortcut/smart/share_doc.go:38
visible_flags: 3

## Flags
- --to <String>: 收件人姓名/花名
- --url <String>: 文档链接
- --note <String>: 附言（可选）

## Related
- dws doc +access-change
- dws doc +access-grant
- dws doc +access-revoke
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
