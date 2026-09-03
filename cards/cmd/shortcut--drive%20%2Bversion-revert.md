# dws drive +version-revert

kind: shortcut
completeness: full
usage: dws drive +version-revert
description: 预检并回滚普通文件到指定历史版本
source: internal/shortcut/drive/version_operations.go:139
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
