# dws mail mailbox shared-with-me

kind: command
completeness: full
usage: dws mail mailbox shared-with-me
description: 查询共享给我的邮箱
example: dws mail mailbox shared-with-me
source: internal/helpers/mail.go:205
visible_flags: 2

## Flags
- --limit <Int>: 返回数量上限 (可选)
- --offset <Int>: 偏移量 (可选)

## Related
- dws mail mailbox list
- dws mail mailbox profile
