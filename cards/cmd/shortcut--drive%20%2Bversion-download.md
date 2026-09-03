# dws drive +version-download

kind: shortcut
completeness: full
usage: dws drive +version-download
description: 安全下载普通文件指定历史版本
source: internal/shortcut/drive/version_operations.go:81
visible_flags: 3

## Flags
- --node <String>: 普通文件节点 ID
- --version <Int>: 版本号；--version 必须为正整数
- --output <String>: 工作目录内相对输出路径

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
