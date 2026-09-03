# dws minutes +speaker-replace

kind: shortcut
completeness: full
description: 预检逐字稿中的发言人昵称，替换后重新读回验证
source: internal/shortcut/minutes/alignment.go:220
visible_flags: 5

## Flags
- --id <String>: 听记 taskUuid
- --from <String>: 源发言人昵称
- --to <String>: 目标发言人昵称
- --target-uid <String>: 目标钉钉 UID
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
