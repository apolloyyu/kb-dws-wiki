# dws mail mailbox shared-with-me

kind: command
completeness: full
description: 查询共享给我的邮箱
source: internal/helpers/mail.go:205
visible_flags: 2

## Flags
- --limit <Int>: 返回数量上限 (可选)
- --offset <Int>: 偏移量 (可选)

## Related
- dws mail mailbox list
