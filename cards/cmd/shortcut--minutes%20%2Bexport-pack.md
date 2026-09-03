# dws minutes +export-pack

kind: shortcut
completeness: full
usage: dws minutes +export-pack
description: 把完整听记产物写入受控目录并生成不含签名 URL 的 manifest
source: internal/shortcut/minutes/workflows.go:189
visible_flags: 5

## Flags
- --id <String>: 听记 taskUuid
- --output <String>: 工作目录内的新归档目录
- --artifacts <StringSlice>: 要导出的产物
- --include-media <Bool>: 同时下载音视频
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
- dws minutes +mindmap
