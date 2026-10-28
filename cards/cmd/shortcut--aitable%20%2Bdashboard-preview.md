# dws aitable +dashboard-preview

kind: shortcut
completeness: full
usage: dws aitable +dashboard-preview
description: 读取真实布局，预览服务端按行重排的逐卡位置和尺寸变化
source: internal/shortcut/aitable/layout_protocol.go:17
visible_flags: 3

## Flags
- --base-id <String>: Base ID
- --dashboard-id <String>: Dashboard ID
- --is-app-mode <Bool>: 已确认的应用模式只读上下文

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
