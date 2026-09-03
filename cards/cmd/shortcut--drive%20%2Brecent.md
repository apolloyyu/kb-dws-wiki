# dws drive +recent

kind: shortcut
completeness: full
description: 获取最近访问/编辑的文档列表
source: internal/shortcut/drive/drive.go:604
visible_flags: 7

## Flags
- --operate-type <Int>: 操作类型: 0=最近访问(默认), 1=最近编辑
- --creator-type <Int>: 创建人过滤: 0=全部, 1=我创建, 2=他人创建
- --limit <Int>: 每页数量 (默认 20，最大 20)
- --cursor <String>: 分页游标 (从上次结果的 nextCursor 获取)
- --page-all <Bool>: 有界读取全部后续页；--max-pages/--max-items 仅在 --page-all 时生效且必须大于 0
- --max-pages <Int>: —
- --max-items <Int>: —

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
