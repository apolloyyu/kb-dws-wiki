# dws drive +version-get

kind: shortcut
completeness: full
usage: dws drive +version-get
description: 按版本号精确读取普通文件版本元数据
source: internal/shortcut/drive/version_operations.go:46
visible_flags: 2

## Flags
- --node <String>: 普通文件节点 ID
- --version <Int>: 版本号；--version 必须为正整数

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
