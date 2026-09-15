# dws aitable +dashboard-list

kind: shortcut
completeness: full
usage: dws aitable +dashboard-list
description: 从完整 Base 目录读取仪表盘列表并验证每项 ID
source: internal/shortcut/aitable/parity_dashboard.go:14
visible_flags: 9

## Flags
- --base-id <String>: Base ID
- --name <String>: 仪表盘名称
- --config <String>: 可选完整 Dashboard config；name 参数覆盖同名属性
- --dashboard-id <String>: Dashboard ID
- --layout <String>: 根布局 JSON，自动从真实 Dashboard 选择 12/48 列
- --is-app-mode <Bool>: 已知应用模式时按 48 列校验，只读上下文

## Related
- dws aitable +advperm-disable
- dws aitable +advperm-enable
- dws aitable +attachment-put
- dws aitable +attachment-remove
- dws aitable +attachment-upload
- dws aitable +base-bootstrap
