# dws drive +star-list

kind: shortcut
completeness: full
usage: dws drive +star-list
description: 严格分页列出当前用户收藏
source: internal/shortcut/drive/catalog_operations.go:278
visible_flags: 3

## Flags
- --limit <Int>: —
- --cursor <String>: 分页游标
- --content-types <StringSlice>: 内容类型过滤

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +find-file
