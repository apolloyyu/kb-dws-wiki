# dws whiteboard +update

kind: shortcut
completeness: full
description: 确认后更新白板并按同一稳定目标精确读回
source: internal/shortcut/whiteboard/whiteboard.go:228
visible_flags: 3

## Flags
- --node <String>: 承载白板的钉钉文档 ID 或 URL；--node 去除空白后不能为空
- --part-id <String>: 文档内白板 part ID；--part-id 去除空白后不能为空
- --source <String>: OpenNodes V1 JSON，不能为空；支持字面量、@相对文件或 - 从 stdin 读取

## Related
- dws whiteboard +query
