# dws aitable view update timebar

kind: command
completeness: full
usage: dws aitable view update timebar
description: 更新视图 timebar 配置（仅 Gantt）
example: dws aitable view update timebar --base-id BASE_ID --table-id TABLE_ID --view-id VIEW_ID --start-field fldStart --end-field fldEnd --timeline-scale month
source: internal/helpers/aitable.go:4286
visible_flags: 7

## Flags
- --start-field <String>: 开始日期字段 ID
- --end-field <String>: 结束日期字段 ID
- --display-field-id <String>: 时间条上显示的标题字段 ID
- --timeline-scale <String>: 时间尺度: year|quarter|month|weeks
- --color-configs <String>: 颜色配置 JSON 数组
- --official-holiday <Bool>: 是否标注法定节假日
- --json <String>: 完整 ganttTimebar 子块 JSON

## Related
- dws aitable view update aggregate
- dws aitable view update card
- dws aitable view update field-widths
- dws aitable view update fill-color-rule
- dws aitable view update filter
- dws aitable view update frozen-cols
