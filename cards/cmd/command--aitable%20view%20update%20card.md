# dws aitable view update card

kind: command
completeness: full
usage: dws aitable view update card
description: 更新视图 card 配置（Kanban / Gallery）
example: dws aitable view update card --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --cover-field-id fldXXX --cover-resize-mode contain
source: internal/helpers/aitable.go:4218
visible_flags: 7

## Flags
- --cover-field-id <String>: 封面字段 ID (Kanban / Gallery 通用)
- --no-cover <Bool>: 清除封面 (Kanban / Gallery 通用)；与 --cover-field-id 互斥
- --cover-resize-mode <String>: 封面缩放: cover|contain|stretch
- --hidden-field-title <Bool>: 隐藏字段名标题 (仅 Kanban)
- --cover-mode <String>: 封面模式 (仅 Gallery): none|auto|custom
- --display-field-name <Bool>: 是否显示字段名 (仅 Gallery)
- --json <String>: 完整 card 子块 JSON，与 typed flag 同时存在时 typed flag 优先

## Related
- dws aitable view update aggregate
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
- dws aitable view update group
