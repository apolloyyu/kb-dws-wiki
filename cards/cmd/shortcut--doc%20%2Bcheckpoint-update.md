# dws doc +checkpoint-update

kind: shortcut
completeness: full
usage: dws doc +checkpoint-update
description: 先保存可回滚版本，再更新并读回验证
source: internal/shortcut/doc/content_shortcuts.go:553
visible_flags: 4

## Flags
- --force <Bool>: 仅全文覆盖：允许使本人待处理建议失效；独立于 --yes
- --node <String>: 文档 ID 或 URL
- --mode <String>: —
- --content <String>: —

## Related
- dws doc +access-change
- dws doc +access-grant
- dws doc +access-revoke
- dws doc +background-delete
- dws doc +background-update
- dws doc +comment-create
