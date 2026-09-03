# dws drive +version-history

kind: shortcut
completeness: full
usage: dws drive +version-history
description: 严格分页列出普通文件历史版本
source: internal/shortcut/drive/version_operations.go:16
visible_flags: 3

## Flags
- --node <String>: 普通文件节点 ID
- --limit <Int>: —
- --cursor <String>: 分页游标

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
