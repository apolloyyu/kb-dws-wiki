# dws minutes +prepare-asr

kind: shortcut
completeness: full
description: 读取个人热词、只新增缺失项并读回验证
source: internal/shortcut/minutes/workflows.go:147
visible_flags: 2

## Flags
- --words <StringSlice>: 目标热词，逗号分隔
- --sync <Bool>: [兼容提示] 已迁移，请使用 +sync-asr

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
