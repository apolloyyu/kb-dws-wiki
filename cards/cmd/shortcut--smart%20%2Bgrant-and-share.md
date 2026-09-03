# dws smart +grant-and-share

kind: shortcut
completeness: full
description: 确保目标角色后按姓名逐人发送文档链接
source: internal/shortcut/smart/doc_access.go:177
visible_flags: 6

## Flags
- --url <String>: 文档链接
- --note <String>: 附言
- --node <String>: 文档 ID 或 URL
- --to <StringSlice>: 协作者姓名列表
- --role <String>: —
- --workspace <String>: 可选知识库 ID

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
