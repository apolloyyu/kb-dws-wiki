# dws minutes +summary

kind: shortcut
completeness: full
usage: dws minutes +summary
description: 读取当前纪要、校验图片引用、全量覆盖并读回验证
source: internal/shortcut/minutes/alignment.go:202
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid
- --content <String>: 完整纪要字面量、@相对文件或 - 表示 stdin

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
