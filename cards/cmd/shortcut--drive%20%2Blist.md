# dws drive +list

kind: shortcut
completeness: full
usage: dws drive +list
description: 严格分页列出钉盘文件和文件夹
source: internal/shortcut/drive/drive.go:40
visible_flags: 10

## Flags
- --space-id <String>: 钉盘空间 ID (纯数字)，不传则使用「我的文件」
- --folder <String>: 父节点 ID (dentryUuid)，不传则列出空间根目录
- --limit <Int>: —
- --cursor <String>: 分页游标，首次不传
- --page-all <Bool>: 有界读取全部后续页；--max-pages/--max-items 仅在 --page-all 时生效且必须大于 0
- --max-pages <Int>: —
- --max-items <Int>: —
- --order-by <String>: 排序字段: createTime|modifyTime|name
- --order <String>: 排序方向: asc|desc (默认 desc)
- --thumbnail <Bool>: 是否返回缩略图信息

## Related
- dws drive +copy
- dws drive +create-folder
- dws drive +create-shortcut
- dws drive +delete
- dws drive +download
- dws drive +info
