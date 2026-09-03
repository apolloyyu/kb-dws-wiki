# dws minutes +sync-asr

kind: shortcut
completeness: full
description: 把个人热词精确同步为目标集合，删除多余项后读回验证
source: internal/shortcut/minutes/workflows.go:172
visible_flags: 1

## Flags
- --words <StringSlice>: 同步后的完整目标热词集合，逗号分隔

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
