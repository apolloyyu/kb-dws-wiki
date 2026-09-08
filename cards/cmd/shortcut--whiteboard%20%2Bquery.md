# dws whiteboard +query

kind: shortcut
completeness: full
usage: dws whiteboard +query
description: 严格读取文档内嵌或独立白板的 OpenNodes 快照
source: internal/shortcut/whiteboard/whiteboard.go:207
visible_flags: 4

## Flags
- --node <String>: 承载文档或独立白板的节点 ID/URL；--node 去除空白后不能为空
- --part-id <String>: 文档内白板 part ID；显式提供时选择内嵌分支。显式非空 --part-id 选择内嵌白板并禁止 view/page-id；未提供时默认独立白板，view=page 必须提供 page-id
- --view <String>: —
- --page-id <String>: 独立白板页面 ID；view=page 时必填。显式非空 --part-id 选择内嵌白板并禁止 view/page-id；未提供时默认独立白板，view=page 必须提供 page-id

## Related
- dws whiteboard +update
