# dws whiteboard +diff

kind: shortcut
completeness: full
usage: dws whiteboard +diff
description: 读取当前白板并预览 proposed OpenNodes 更新的节点、媒体与风险变化
source: internal/shortcut/whiteboard/diff.go:80
visible_flags: 7

## Flags
- --node <String>: 承载文档或独立白板的节点 ID/URL；去除空白后不能为空
- --part-id <String>: 文档内白板 part ID；
- --page-id <String>: 独立白板页面 ID；
- --source <String>: —
- --identity-map <String>: 可选 version=1 逻辑 ID 到当前真实节点 ID 的显式映射；支持字面量、@相对文件或 - 从 stdin 读取
- --comparison <String>: —
- --detail-limit <Int>: —

## Related
- dws whiteboard +query
- dws whiteboard +update
