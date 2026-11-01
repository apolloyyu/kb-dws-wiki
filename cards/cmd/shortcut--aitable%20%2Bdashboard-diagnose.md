# dws aitable +dashboard-diagnose

kind: shortcut
completeness: full
usage: dws aitable +dashboard-diagnose
description: 只读检查根布局几何、指定区域覆盖及声明设计差异
source: internal/shortcut/aitable/layout_diagnostics.go:20
visible_flags: 5

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --expected-layout <String>: 可选完整设计 JSON 数组，每项 i/x/y/w/h 必填；比较全部根卡片，保持叠放设计
- --regions <String>: 可选区域 JSON 数组，每项 id/x/y/w/h 必填，chartIds 可选；核验选中根卡片的并集覆盖
- --is-app-mode <Bool>: 已确认的应用模式上下文

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
