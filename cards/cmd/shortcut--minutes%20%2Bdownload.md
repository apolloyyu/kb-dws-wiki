# dws minutes +download

kind: shortcut
completeness: full
description: 批量取得听记音视频地址并安全下载到本地
source: internal/shortcut/minutes/alignment.go:67
visible_flags: 5

## Flags
- --id <String>: 单个 taskUuid
- --ids <StringSlice>: 多个 taskUuid，最多 50 个
- --url-only <Bool>: 只返回临时签名 URL，不下载
- --output <String>: 单个目标的工作目录内相对输出路径
- --output-dir <String>: —

## Related
- dws minutes +apply-permission
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
- dws minutes +mindmap
