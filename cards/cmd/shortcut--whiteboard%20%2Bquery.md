# dws whiteboard +query

kind: shortcut
completeness: full
usage: dws whiteboard +query
description: 严格读取已有文档白板的 OpenNodes 快照
source: internal/shortcut/whiteboard/whiteboard.go:181
visible_flags: 2

## Flags
- --node <String>: 承载白板的钉钉文档 ID 或 URL；--node 去除空白后不能为空
- --part-id <String>: 文档内白板 part ID；--part-id 去除空白后不能为空

## Related
- dws whiteboard +update
